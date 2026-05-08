# System Architecture

## Overview

The CS326-SIAM system is a user management and authentication platform built with a lightweight two-layer architecture: a Python application core and a Node.js middleware layer. It is designed for simplicity, portability, and ease of deployment on any free-tier cloud platform.

---

## Architecture Diagram

```
┌─────────────────────────────────────────────────────────┐
│                        CLIENT                           │
│              (Browser / API Consumer)                   │
└───────────────────────┬─────────────────────────────────┘
                        │ HTTP Requests
                        ▼
┌─────────────────────────────────────────────────────────┐
│                  Node.js Layer (app.js)                 │
│  ┌──────────────────┐   ┌──────────────────────────┐   │
│  │ Auth Middleware  │   │ Input Validation Layer   │   │
│  │ (Token check)    │   │ (Login, Register routes) │   │
│  └──────────────────┘   └──────────────────────────┘   │
└───────────────────────┬─────────────────────────────────┘
                        │ Internal Logic Calls
                        ▼
┌─────────────────────────────────────────────────────────┐
│               Python Application Core                   │
│  ┌─────────────┐  ┌──────────────┐  ┌───────────────┐  │
│  │  register() │  │   login()    │  │update_profile()│  │
│  └─────────────┘  └──────────────┘  └───────────────┘  │
│                         │                               │
│              ┌──────────▼──────────┐                   │
│              │   Logging Module    │                    │
│              │  (app.log / INFO,   │                    │
│              │   WARNING events)   │                    │
│              └─────────────────────┘                   │
└─────────────────────────────────────────────────────────┘
                        │ Writes to
                        ▼
┌─────────────────────────────────────────────────────────┐
│                     Data Layer                          │
│              app.log  (structured log file)             │
└─────────────────────────────────────────────────────────┘
```

---

## Component Breakdown

### 1. Node.js Layer (`app.js`)
**Responsibility:** HTTP routing, authentication middleware, and input validation.

| Component | Description |
|-----------|-------------|
| `basicAuth` middleware | Validates `Authorization` header token before granting access |
| `/login` route | Validates username/password format and length |
| Input sanitization | Rejects empty or out-of-range inputs with 400 errors |

**Tech:** Node.js (Express-compatible), plain JavaScript

---

### 2. Python Application Core (`project/code/app/user.py`)
**Responsibility:** Business logic for user operations.

| Function | Description |
|----------|-------------|
| `register(username, password)` | Validates non-empty fields; creates account |
| `login(username, password)` | Validates credentials against known values |
| `update_profile(name)` | Enforces minimum name length (≥ 2 characters) |

**Tech:** Python 3, standard library only (no external dependencies)

---

### 3. Logging Module
**Responsibility:** Persistent event recording for KPI tracking and debugging.

- Output file: `project/code/app/app.log`
- Format: `%(asctime)s - %(levelname)s - %(message)s`
- Levels used: `INFO` (success events), `WARNING` (validation failures)

---

### 4. Test Suite (`project/code/tests/test_user.py`)
**Responsibility:** Automated unit testing of all core business logic.

| Test | Validates |
|------|-----------|
| `test_register_success` | Valid registration returns `True` |
| `test_register_fail_empty` | Empty fields return `False` |
| `test_login_success` | Correct credentials return `True` |
| `test_login_fail` | Wrong password returns `False` |
| `test_update_profile_valid` | Valid name returns `True` |

**Tech:** pytest

---

### 5. CI/CD Pipeline (`.github/workflows/`)

| Workflow | Trigger | Steps |
|----------|---------|-------|
| `ci.yml` | Push to `main` | Checkout → Install deps → Run tests → Security audit |
| `deploy.yml` | Push to `main` | Checkout → `npm audit` → Deploy → Smoke test |

**Tech:** GitHub Actions, ubuntu-latest runners

---

## Technology Stack

| Layer | Technology | Rationale |
|-------|-----------|-----------|
| Backend logic | Python 3 | Simple, readable, cross-platform |
| Middleware / API | Node.js | Lightweight HTTP handling |
| CI/CD | GitHub Actions | Free, integrated with repo, no external tools needed |
| Version control | Git / GitHub | Industry standard, enables automation |
| Logging | Python `logging` module | Zero-dependency structured logging |
| Testing | pytest | Simple, powerful, widely used |
| Secret management | `.env` + `.gitignore` | Prevents credential leakage |

---

## Cloud Deployment Strategy

The system is designed to deploy to any free-tier PaaS provider with zero configuration changes:

| Platform | Deployment Method | Cost |
|----------|------------------|------|
| **Railway** | Connect GitHub repo → auto-deploy on push | Free tier |
| **Render** | Web service → GitHub integration | Free tier |
| **Fly.io** | `fly deploy` via CLI | Free tier |
| **GitHub Pages** (static only) | Push to `gh-pages` branch | Free |

### Deployment Flow
```
Developer pushes to main
        │
        ▼
GitHub Actions CI runs
        │
   ┌────┴────┐
   │  Tests  │ ← pytest (Python unit tests)
   │  pass?  │
   └────┬────┘
        │ Yes
        ▼
   npm audit (security check)
        │
        ▼
   Deploy to cloud platform
        │
        ▼
   Smoke test (HTTP check)
        │
        ▼
   Live ✅
```

---

## Emerging Technologies Considered

| Technology | Relevance | Status |
|-----------|-----------|--------|
| **Containerization (Docker)** | Package app + dependencies for portable deployment | Planned (post-MVP) |
| **AI-assisted code review** | GitHub Copilot / Gemini for PR suggestions | In use during development |
| **Automated security scanning** | `npm audit` + GitHub Dependabot | Active in CI |
| **Log-based observability** | Structured logging → future integration with Datadog/Grafana | Foundation laid (app.log) |
| **Serverless functions** | Route handlers could migrate to AWS Lambda / Vercel Functions | Applicable to Node.js layer |

---

## Security Design Decisions

| Decision | Rationale |
|----------|-----------|
| Token in `Authorization` header | Standard HTTP auth pattern, easy to rotate |
| `.env` for secrets + `.gitignore` | Prevents secrets from entering version control |
| Input length validation at API layer | Prevents buffer overflows and injection-style attacks |
| `npm audit` in CI | Catches known vulnerabilities in dependencies before deployment |
| Python `logging` instead of `print` | Produces persistent, structured audit trails |
