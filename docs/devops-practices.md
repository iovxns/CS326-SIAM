# DevOps Practices

## Overview

This document describes the DevOps practices adopted throughout the CS326-SIAM project, covering version control, CI/CD pipeline design, testing strategy, security, deployment, and observability. These practices align with modern software engineering standards and emerging cloud-native trends.

---

## 1. Version Control

**Tool:** Git + GitHub

| Practice | Description |
|----------|-------------|
| Feature branching | Each feature developed on its own branch before merging to `main` |
| Pull request reviews | PRs reviewed by at least one team member before merge |
| PR template | `.github/pull_request_template.md` ensures consistent PR descriptions |
| Issue templates | `.github/ISSUE_TEMPLATES/` standardizes bug and feature request reporting |
| `.gitignore` | Excludes `node_modules/`, `.env`, log files, and `__pycache__` from commits |
| Semantic versioning | Releases tagged using `vMAJOR.MINOR.PATCH` (e.g., `v1.0.0`) |

---

## 2. Continuous Integration (CI)

**Tool:** GitHub Actions

### CI Workflow (`ci.yml`)

Triggered on every push to `main` and on pull requests.

```
Push / PR to main
      │
      ▼
┌─────────────────┐
│ Checkout Code   │  actions/checkout@v4
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ Set up Python   │  actions/setup-python@v5 (Python 3.x)
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ Install pytest  │  pip install pytest
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  Run Tests      │  pytest project/code/tests/
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ Security Audit  │  npm audit --audit-level=high
└────────┬────────┘
         │
         ▼
       CI ✅
```

### CI Principles Applied
- **Fail fast:** Tests run before any deployment step — broken code never ships.
- **Audit on every push:** `npm audit` catches newly disclosed vulnerabilities automatically.
- **No manual gates:** The pipeline is fully automated; no human needs to approve a CI run.

---

## 3. Continuous Deployment (CD)

**Tool:** GitHub Actions (`deploy.yml`)

Triggered on push to `main` after CI passes.

| Step | Description |
|------|-------------|
| Checkout | Fresh copy of repo on runner |
| Security audit | `npm audit --audit-level=high` — blocks deployment on high-severity issues |
| Deploy | Platform-specific deploy command (e.g., `railway up`, `render deploy`) |
| Smoke test | `curl -I --fail <app-url>` — verifies the deployed app responds with HTTP 2xx |

### Deployment Target Options

| Platform | Command | Notes |
|----------|---------|-------|
| Railway | `railway up` | Free tier, auto-detects runtime |
| Render | Push to `main` (auto-deploy) | Connected via GitHub integration |
| Fly.io | `fly deploy` | Requires `fly.toml` config |

---

## 4. Testing Strategy

**Framework:** pytest (Python)

### Test Coverage

| Test | Type | What it validates |
|------|------|------------------|
| `test_register_success` | Unit | Happy path — valid registration |
| `test_register_fail_empty` | Unit | Edge case — empty input rejected |
| `test_login_success` | Unit | Happy path — correct credentials accepted |
| `test_login_fail` | Unit | Edge case — wrong password rejected |
| `test_update_profile_valid` | Unit | Happy path — valid name accepted |

### Running Tests Locally

```bash
# From project root
cd project/code
pytest tests/ -v
```

### Testing Principles
- **Arrange-Act-Assert pattern:** Each test is independent and self-contained.
- **No external dependencies:** Tests run with zero network access or database.
- **CI-integrated:** Tests automatically run on every push via GitHub Actions.

---

## 5. Security Practices

| Practice | Implementation |
|----------|---------------|
| Secret management | Secrets stored in `.env`; `.gitignore` prevents accidental commits |
| Dependency scanning | `npm audit` runs in CI on every push |
| Input validation | All user inputs validated for length and non-empty before processing |
| Token-based auth | `Authorization` header token checked before route access |
| Principle of least privilege | Each function does exactly one thing; no over-permissioned logic |
| Audit logging | All auth events (success and failure) logged with timestamps to `app.log` |

---

## 6. Observability & Logging

**Tool:** Python `logging` module → `app.log`

### Log Levels Used

| Level | Events logged |
|-------|--------------|
| `INFO` | Successful registrations, logins, profile updates |
| `WARNING` | Failed logins, validation failures, invalid inputs |

### Log Format

```
2026-05-08 12:34:56,789 - INFO - Login successful
2026-05-08 12:34:57,001 - WARNING - Login failed: Invalid credentials
```

### Future Observability Improvements
- Integrate with **Grafana + Loki** for log aggregation and dashboards
- Add **structured JSON logging** for easier parsing
- Introduce **correlation IDs** per user session for end-to-end request tracing

---

## 7. Infrastructure as Code (IaC)

Current state: Lightweight, minimal config.

| Config file | Purpose |
|-------------|---------|
| `.github/workflows/ci.yml` | Defines the CI pipeline declaratively |
| `.github/workflows/deploy.yml` | Defines the CD pipeline declaratively |
| `.gitignore` | Declares what should never enter version control |
| `package-lock.json` | Pins exact dependency versions for reproducible builds |

### Planned IaC Improvements
- Add `Dockerfile` to containerize the application for portable, reproducible deployment
- Add `docker-compose.yml` for local multi-service development
- Consider `terraform` or `fly.toml` for cloud infrastructure provisioning

---

## 8. Emerging Trends Applied

| Trend | How it's applied in this project |
|-------|----------------------------------|
| **AI-assisted development** | GitHub Copilot / Gemini used during coding and documentation |
| **Shift-left security** | Security audit (`npm audit`) runs in CI, not post-deployment |
| **GitOps** | All infrastructure changes (CI/CD config) are version-controlled in Git |
| **Observability-first design** | Logging is built in from day one, not added as an afterthought |
| **Zero-cost cloud** | Free-tier platforms (Railway, Render) enable cloud deployment without budget |
| **Automated compliance** | PR templates and issue templates enforce team standards automatically |

---

## 9. DevOps Maturity Assessment

| Dimension | Current Level | Target |
|-----------|--------------|--------|
| Version control | ✅ Git + GitHub, branching, PRs | Maintained |
| CI | ✅ Automated tests + security audit | Add coverage reporting |
| CD | ⚠️ Partially configured (smoke test URL placeholder) | Connect live deployment URL |
| Testing | ✅ Unit tests passing | Add integration tests |
| Security | ✅ Audit in CI, secrets in `.env` | Add SAST scanning (e.g., CodeQL) |
| Observability | ⚠️ Local log file only | Centralized log aggregation |
| Containerization | ❌ Not yet implemented | Add Dockerfile |
| IaC | ⚠️ CI/CD config only | Add cloud provisioning config |

---

## 10. Release Management

| Practice | Description |
|----------|-------------|
| Semantic versioning | Format: `vMAJOR.MINOR.PATCH` |
| Git tags | Each release tagged: `git tag v1.0.0 && git push origin v1.0.0` |
| Changelog | Future: maintain `CHANGELOG.md` per release |
| Current release | `v1.0` — MVP with registration, login, profile update, CI/CD, and logging |
