# Changelog

All notable project changes are documented here.

## [1.0.0] - 2026-11-06

### Added

- A searchable Quarto website with letter indexes, per-letter entry pages,
  related-term links, and responsive navigation.
- 347 unique AI engineering dictionary entries across A–Z, with layered
  explanations, practical examples, references, and selected explanatory SVGs.
- Practical Jupyter notebooks for selected concepts.
- GitHub issue forms for bug reports, terminology proposals, and definition
  improvements, plus a pull request checklist.
- Entry metadata and duplicate-term validation through
  `scripts/validate_entries.py`.
- Vercel static deployment configuration with a pinned, checksum-verified
  Quarto CLI build and documented Git-based production and preview deployments.

### Changed

- Reconciled the master vocabulary and CSV with the existing Decoupling and
  Jacobian entry pages.
- Updated the contribution guide and README to describe the current project
  structure and workflow.

### Deployment status

- Vercel configuration is ready for manual project setup. The website has not
  been deployed and this release has not been published.
