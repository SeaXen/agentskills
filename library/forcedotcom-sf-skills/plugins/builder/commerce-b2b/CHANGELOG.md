# Changelog

All notable changes to this plugin are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this plugin adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.1.2] — 2026-10-02

### Changed

- The bundled skills now match the standalone versions published in this repository. Both skills
  read your project's package directory from `sfdx-project.json` themselves, without a bundled
  helper script.

## [0.1.1] — 2026-09-21

### Changed

- Both skills now use your project's package directory from `sfdx-project.json` (the default
  entry, or the first one) instead of assuming a fixed path.
- Skill descriptions now state more clearly when each skill applies and when to use another skill
  instead.

### Fixed

- `commerce-b2b-open-code-components-integrate` can now run the Salesforce CLI commands it needs
  without extra permission prompts.

## [0.1.0] — 2026-08-24

### Added

- Initial release. Integrate the official Salesforce B2B Commerce open-source component library
  into a store's site metadata (`commerce-b2b-open-code-components-integrate`), and map or replace
  out-of-the-box commerce components with their open-code equivalents
  (`commerce-b2b-open-code-components-replace`).
