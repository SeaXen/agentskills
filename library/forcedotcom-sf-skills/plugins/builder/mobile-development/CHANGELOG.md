# Changelog

All notable changes to this plugin are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this plugin adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.2.1] — 2026-09-21

### Fixed

- When you build an app that embeds Agentforce, `mobile-apps-create` now always loads the
  Agentforce SDK skill for your platform instead of hand-writing the integration, which could
  produce code that didn't compile.

## [0.2.0] — 2026-08-26

### Added

- Initial release. Scaffold new Mobile SDK apps or add Mobile SDK to existing iOS and Android apps,
  with Salesforce authentication, biometric login, and embedded Agentforce (`mobile-apps-create`);
  integrate native device capabilities (`mobile-platform-native-capabilities-integrate`); and
  validate offline storage and sync with SmartStore and MobileSync
  (`mobile-platform-offline-validate`).
