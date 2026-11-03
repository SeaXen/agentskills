#!/usr/bin/env python3
"""
Risk and position-sizing helper for Hermes crypto workflows.
Supports both One-Way and Hedge mode.
"""

import argparse
import json
import sys
from typing import Any, Dict, List, Optional


def print_json(obj: Any) -> None:
    print(json.dumps(obj, indent=2))


def rr(entry: float, stop: float, target: float) -> float:
    risk_per_unit = abs(entry - stop)
    reward_per_unit = abs(target - entry)
    if risk_per_unit == 0:
        return 0
    return reward_per_unit / risk_per_unit


def calculate_side(equity: float, risk_amount: float, entry: float, stop: float, targets: List[float], side: str):
    if entry == stop:
        return {"error": "Entry and Stop cannot be equal"}
    
    stop_distance = abs(entry - stop)
    position_units = risk_amount / stop_distance
    notional = position_units * entry
    
    res = {
        "side": side,
        "entry": entry,
        "stop": stop,
        "stop_distance": stop_distance,
        "position_units": position_units,
        "position_notional": notional,
        "max_loss": risk_amount,
        "targets": []
    }
    
    for t in targets:
        res["targets"].append({
            "target": t,
            "rr": rr(entry, stop, t),
            "profit": abs(t - entry) * position_units
        })
    return res


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--equity", type=float, required=True)
    parser.add_argument("--risk-pct", type=float)
    parser.add_argument("--risk-amount", type=float)
    
    # Long parameters
    parser.add_argument("--entry", type=float)
    parser.add_argument("--stop", type=float)
    parser.add_argument("--target", type=float, action="append")
    
    # Short parameters (Hedge Mode)
    parser.add_argument("--short-entry", type=float)
    parser.add_argument("--short-stop", type=float)
    parser.add_argument("--short-target", type=float, action="append")
    
    parser.add_argument("--mode", default="one-way", choices=["one-way", "hedge"])
    parser.add_argument("--side", default="long") # Backward compatibility
    
    args = parser.parse_args()
    
    risk_amount = args.risk_amount
    if risk_amount is None:
        if args.risk_pct is None:
            sys.exit("Provide --risk-amount or --risk-pct")
        risk_amount = args.equity * (args.risk_pct / 100.0)

    out = {
        "mode": args.mode,
        "equity": args.equity,
        "total_risk_amount": risk_amount,
        "long": None,
        "short": None,
        "side": args.side
    }
    
    if args.entry is not None and args.stop is not None:
        out["long"] = calculate_side(args.equity, risk_amount, args.entry, args.stop, args.target or [], "long")
        
    if args.mode == "hedge" and args.short_entry is not None and args.short_stop is not None:
        out["short"] = calculate_side(args.equity, risk_amount, args.short_entry, args.short_stop, args.short_target or [], "short")
        
    if args.mode == "one-way" and out["long"]:
        # Flat legacy mapping
        for k, v in out["long"].items():
            out[k] = v
        out["risk_pct"] = (risk_amount / args.equity * 100.0) if args.equity else None
        out["risk_amount"] = risk_amount
        out["max_loss_if_stopped"] = risk_amount

    print_json(out)


if __name__ == "__main__":
    main()
