# Changelog

All notable changes to this plugin are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this plugin adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.1.1] — 2026-10-02

### Removed

- Dev Hub administration (`dx-org-devhub-configure`) is no longer bundled with this plugin.
  Install the `dx-org-lifecycle` plugin to keep enabling Dev Hub and viewing scratch org
  allocation.

### Changed

- The bundled `dx-app-analytics-query` skill now matches the standalone version published in this
  repository.

## [0.1.0] — 2026-08-24

### Added

- Initial release. Enable or inspect Dev Hub and scratch org allocation (`dx-org-devhub-configure`),
  request managed-package App Analytics usage data or subscriber snapshots and configure App
  Analytics settings (`dx-app-analytics-query`), and enable or disable receiving Transactable
  Marketplace partner offers (`platform-agentexchange-partner-offers-configure`).
