#!/usr/bin/env python3
"""Schema validation for the security-audit artefacts, in pure Python.

The absorbed `security-audit` validators are Node programs that refuse to run
where the OS cannot offer no-follow, nonblocking file reads - which is the
case on Windows.  Rather than let the deep security mode be skipped on a whole
platform, this module re-implements the two checks in Python:

* `validate_findings(instance, schema)` - a JSON-Schema subset validator for
  `report-schema.json` (type, required, properties, additionalProperties,
  oneOf, items, pattern, minItems, minLength, minimum, enum, const,
  uniqueItems and the custom `visibleContent` keyword).
* `validate_ledger(ledger)` - the structural rules of the coverage ledger
  (required fields, canonical coverage id, statuses, attempt waves, evidence
  invariants, reviewed-path ownership, path safety, ordering).

Both return a list of human-readable errors: an empty list means valid.

The Node validators stay authoritative where they can run; this module is the
portable fallback and the cross-check.
"""
from __future__ import annotations

import re

TYPES = {
    "object": dict,
    "array": list,
    "string": str,
    "boolean": bool,
    "number": (int, float),
    "integer": int,
    "null": type(None),
}

LEDGER_REQUIRED_FIELDS = (
    "coverage_id", "canonical_refs", "surface", "boundary", "subsystem",
    "attack_class", "starting_paths", "ordinary_attack_class_block",
    "selected_companion_blocks", "excluded_blocks", "prior_status",
    "attempts", "wave", "status", "agent_id", "reviewed_paths",
    "local_checks", "result_fingerprints", "unresolved",
)
LEDGER_REF_FIELDS = ("surface", "boundary", "subsystem", "attack_class")
LEDGER_STATUSES = {"planned", "not_applicable", "out_of_scope", "in_progress",
                   "covered", "candidate", "blocked", "deferred"}
LEDGER_PRIOR_STATUSES = {"new", "prior_confirmed_same_source",
                         "prior_confirmed_changed_source",
                         "prior_needs_validation", "prior_deferred",
                         "prior_blocked", "prior_out_of_scope",
                         "prior_covered_same_source",
                         "prior_covered_changed_source",
                         "prior_rejected_claim_changed", "none"}
LEDGER_ATTEMPT_STATUSES = {"covered", "candidate", "blocked"}
LEDGER_ATTEMPT_FIELDS = ("wave", "status", "agent_id", "reviewed_paths",
                         "local_checks", "result_fingerprints", "unresolved",
                         "reassignment_reason")
AGENT_ID_RE = re.compile(r"^[a-z0-9][a-z0-9_-]{0,63}$")
WINDOWS_RESERVED = re.compile(r"^(?:con|prn|aux|nul|com[1-9]|lpt[1-9])$")
FINGERPRINT_RE = re.compile(r"^[A-Za-z0-9][A-Za-z0-9._:/@+-]*$")
UNRESERVED = set("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
                 "0123456789-._~")


def _visible(value) -> bool:
    return bool(re.search(r"[^\s\x00-\x1f\x7f]", str(value)))


def _type_ok(value, name) -> bool:
    expected = TYPES.get(name)
    if expected is None:
        return True
    if name == "boolean":
        return isinstance(value, bool)
    if name in ("number", "integer") and isinstance(value, bool):
        return False
    if name == "integer":
        return isinstance(value, int)
    return isinstance(value, expected)


def _validate_node(value, schema, path, errors):
    if not isinstance(schema, dict):
        return
    if "oneOf" in schema:
        matches = 0
        branch_errors = []
        for index, branch in enumerate(schema["oneOf"]):
            sub = []
            _validate_node(value, branch, f"{path}", sub)
            if not sub:
                matches += 1
            else:
                branch_errors.append(f"branch {index}: {sub[0]}")
        if matches != 1:
            detail = "; ".join(branch_errors[:3])
            errors.append(f"{path}: must match exactly one schema branch "
                          f"(matched {matches}) {detail}")
        return

    if "type" in schema:
        expected = schema["type"]
        names = expected if isinstance(expected, list) else [expected]
        if not any(_type_ok(value, name) for name in names):
            errors.append(f"{path}: expected type {expected}")
            return

    if "const" in schema and value != schema["const"]:
        errors.append(f"{path}: expected the constant {schema['const']!r}")
    if "enum" in schema and value not in schema["enum"]:
        errors.append(f"{path}: {value!r} is not one of {schema['enum']}")

    if isinstance(value, str):
        if "minLength" in schema and len(value) < schema["minLength"]:
            errors.append(f"{path}: shorter than {schema['minLength']} characters")
        if "pattern" in schema and not re.search(schema["pattern"], value):
            errors.append(f"{path}: does not match {schema['pattern']!r}")
        if schema.get("visibleContent") and not _visible(value):
            errors.append(f"{path}: must contain visible prose")

    if isinstance(value, (int, float)) and not isinstance(value, bool):
        if "minimum" in schema and value < schema["minimum"]:
            errors.append(f"{path}: below the minimum {schema['minimum']}")

    if isinstance(value, list):
        if "minItems" in schema and len(value) < schema["minItems"]:
            errors.append(f"{path}: needs at least {schema['minItems']} item(s)")
        if schema.get("uniqueItems") and len({repr(v) for v in value}) != len(value):
            errors.append(f"{path}: items must be unique")
        item_schema = schema.get("items")
        if isinstance(item_schema, dict):
            for index, item in enumerate(value):
                _validate_node(item, item_schema, f"{path}[{index}]", errors)

    if isinstance(value, dict):
        for field in schema.get("required", []):
            if field not in value:
                errors.append(f"{path}: missing required field {field!r}")
        properties = schema.get("properties") or {}
        if schema.get("additionalProperties") is False:
            for key in value:
                if key not in properties:
                    errors.append(f"{path}: unexpected field {key!r}")
        for key, sub_schema in properties.items():
            if key in value:
                _validate_node(value[key], sub_schema, f"{path}.{key}", errors)


def validate_findings(instance, schema) -> list:
    """Validate a findings document (a list of records) against the schema."""
    errors = []
    if not isinstance(instance, list):
        return ["findings: the document must be an array of findings"]
    if isinstance(schema, dict) and ("items" in schema or schema.get("type") == "array"):
        _validate_node(instance, schema, "findings", errors)
        return errors
    for index, record in enumerate(instance):
        _validate_node(record, schema, f"findings[{index}]", errors)
    return errors


def _encode_ref(value: str) -> str:
    out = []
    for byte in str(value).encode("utf-8"):
        char = chr(byte)
        if char in UNRESERVED:
            out.append(char)
        else:
            out.append("%%%02X" % byte)
    return "".join(out)


def canonical_coverage_id(refs: dict) -> str:
    """The canonical id of a coverage unit (same rule as the Node validator)."""
    fields = list(LEDGER_REF_FIELDS)
    if "lifecycle" in refs:
        fields.append("lifecycle")
    return "::".join(_encode_ref(refs[field]) for field in fields)


def _safe_path(value) -> bool:
    if not isinstance(value, str) or not value or value.strip() != value:
        return False
    if "\\" in value or ":" in value or value.startswith("/"):
        return False
    parts = value.split("/")
    return all(part and part not in (".", "..") for part in parts)


def _check_evidence(node, base, errors, require_fingerprints):
    status = node.get("status")
    reviewed = node.get("reviewed_paths")
    checks = node.get("local_checks")
    fingerprints = node.get("result_fingerprints")
    unresolved = node.get("unresolved")
    if status == "covered":
        if not reviewed:
            errors.append(f"{base}.reviewed_paths: a covered unit needs reviewed paths")
        if not checks:
            errors.append(f"{base}.local_checks: a covered unit needs at least one check")
        if fingerprints:
            errors.append(f"{base}.result_fingerprints: a covered unit must keep this empty")
        if unresolved:
            errors.append(f"{base}.unresolved: a covered unit must keep this empty")
    elif status == "candidate":
        if not reviewed:
            errors.append(f"{base}.reviewed_paths: a candidate unit needs reviewed paths")
        if not checks:
            errors.append(f"{base}.local_checks: a candidate unit needs at least one check")
        if not fingerprints:
            errors.append(f"{base}.result_fingerprints: a candidate unit needs its fingerprints")
    elif status in ("blocked",):
        if not reviewed or not checks or not unresolved:
            errors.append(f"{base}: a blocked unit needs paths, checks and unresolved items")
    elif status in ("planned", "not_applicable", "out_of_scope", "deferred"):
        if node.get("agent_id") is not None:
            errors.append(f"{base}.agent_id: a {status} unit must be unassigned")
        for field in ("reviewed_paths", "local_checks", "result_fingerprints"):
            if node.get(field):
                errors.append(f"{base}.{field}: a {status} unit must keep this empty")
    if status not in LEDGER_STATUSES:
        errors.append(f"{base}.status: unknown status {status!r}")
    if require_fingerprints and status == "covered" and fingerprints:
        pass


def validate_ledger(ledger) -> list:
    """Validate a coverage ledger (a list of units)."""
    errors = []
    if not isinstance(ledger, list):
        return ["coverage ledger: the document must be an array of units"]
    if not ledger:
        return ["coverage ledger: no units"]
    previous_id = None
    for index, unit in enumerate(ledger):
        base = f"ledger[{index}]"
        if not isinstance(unit, dict):
            errors.append(f"{base}: expected an object")
            continue
        for field in LEDGER_REQUIRED_FIELDS:
            if field not in unit:
                errors.append(f"{base}: missing required field {field!r}")
        refs = unit.get("canonical_refs")
        if not isinstance(refs, dict):
            errors.append(f"{base}.canonical_refs: expected an object")
        else:
            expected = list(LEDGER_REF_FIELDS) + (["lifecycle"] if "lifecycle" in refs else [])
            for field in expected:
                if field not in refs:
                    errors.append(f"{base}.canonical_refs: missing {field!r}")
            for field in refs:
                if field not in expected:
                    errors.append(f"{base}.canonical_refs: unexpected field {field!r}")
            try:
                canonical = canonical_coverage_id(refs)
            except KeyError:
                canonical = None
            if canonical and unit.get("coverage_id") != canonical:
                errors.append(f"{base}.coverage_id: expected {canonical!r}")
        if unit.get("status") not in LEDGER_STATUSES:
            errors.append(f"{base}.status: unknown status {unit.get('status')!r}")
        if unit.get("prior_status") not in LEDGER_PRIOR_STATUSES:
            errors.append(f"{base}.prior_status: unknown value {unit.get('prior_status')!r}")
        agent = unit.get("agent_id")
        if agent is not None:
            if not AGENT_ID_RE.match(str(agent)) or WINDOWS_RESERVED.match(str(agent)):
                errors.append(f"{base}.agent_id: {agent!r} is not a canonical agent id")
        for path in unit.get("starting_paths") or []:
            if not _safe_path(path):
                errors.append(f"{base}.starting_paths: {path!r} is not a safe relative path")
        if not unit.get("starting_paths"):
            errors.append(f"{base}.starting_paths: must not be empty")
        for fingerprint in unit.get("result_fingerprints") or []:
            if not FINGERPRINT_RE.match(str(fingerprint)):
                errors.append(f"{base}.result_fingerprints: {fingerprint!r} is not a fingerprint")
        _check_evidence(unit, base, errors, require_fingerprints=True)

        attempts = unit.get("attempts")
        if not isinstance(attempts, list) or not attempts:
            errors.append(f"{base}.attempts: expected a non-empty array")
            continue
        previous_wave = 0
        for a_index, attempt in enumerate(attempts):
            a_base = f"{base}.attempts[{a_index}]"
            if not isinstance(attempt, dict):
                errors.append(f"{a_base}: expected an object")
                continue
            for field in LEDGER_ATTEMPT_FIELDS:
                if field not in attempt:
                    errors.append(f"{a_base}: missing required field {field!r}")
            wave = attempt.get("wave")
            if not isinstance(wave, int) or wave < 1:
                errors.append(f"{a_base}.wave: expected a positive integer")
            else:
                if wave <= previous_wave:
                    errors.append(f"{a_base}.wave: waves must strictly increase")
                if isinstance(unit.get("wave"), int) and wave >= unit["wave"]:
                    errors.append(f"{a_base}.wave: an archived wave must precede the current wave")
                previous_wave = wave
            if attempt.get("status") not in LEDGER_ATTEMPT_STATUSES:
                errors.append(f"{a_base}.status: unknown status {attempt.get('status')!r}")
            attempt_agent = attempt.get("agent_id")
            if not AGENT_ID_RE.match(str(attempt_agent)) or WINDOWS_RESERVED.match(str(attempt_agent)):
                errors.append(f"{a_base}.agent_id: {attempt_agent!r} is not a canonical agent id")
            for path in attempt.get("reviewed_paths") or []:
                if not _safe_path(path):
                    errors.append(f"{a_base}.reviewed_paths: {path!r} is not a safe relative path")
            for check in attempt.get("local_checks") or []:
                if not isinstance(check, dict):
                    errors.append(f"{a_base}.local_checks: expected objects")
                    continue
                for field in ("agent_id", "reviewed_paths", "invariant", "method",
                              "result", "artifact"):
                    if field not in check:
                        errors.append(f"{a_base}.local_checks: missing field {field!r}")
                if check.get("method") not in ("source", "local"):
                    errors.append(f"{a_base}.local_checks: method must be source or local")
                if check.get("method") == "source" and check.get("artifact") is not None:
                    errors.append(f"{a_base}.local_checks: a source check must use a null artifact")
            _check_evidence(attempt, a_base, errors, require_fingerprints=False)

        # reviewed-path ownership: aggregate paths and check paths must match
        aggregate = list(unit.get("reviewed_paths") or [])
        owned = set()
        for check in unit.get("local_checks") or []:
            if isinstance(check, dict):
                owned.update(check.get("reviewed_paths") or [])
        for path in aggregate:
            if path not in owned:
                errors.append(f"{base}.reviewed_paths: {path!r} has no check owner")
        for path in owned:
            if path not in aggregate:
                errors.append(f"{base}.local_checks: owned path {path!r} is absent from reviewed_paths")

        current_id = unit.get("coverage_id")
        if isinstance(current_id, str):
            if previous_id is not None and current_id <= previous_id:
                errors.append(f"{base}.coverage_id: units must be sorted lexicographically")
            previous_id = current_id
    return errors
