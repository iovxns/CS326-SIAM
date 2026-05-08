# Cost–Benefit Analysis & Cost Estimation

## Overview

This document provides a cost–benefit analysis and cost estimation model for the CS326-SIAM User Management System. The system provides core authentication and user management features including registration, login, profile management, and admin controls, developed over a 15-week academic sprint.

---

## 1. Development Cost Estimation

### Assumptions

| Parameter | Value |
|-----------|-------|
| Team size | 4 members |
| Project duration | 15 weeks |
| Average hours per member per week | 10 hrs/week |
| Estimated hourly rate (student/junior dev) | $20/hr |

### Effort Breakdown by Role

| Role | Weeks Active | Hrs/Week | Total Hours | Cost (@ $20/hr) |
|------|-------------|----------|-------------|-----------------|
| PM / Scrum Master | 15 | 10 | 150 | $3,000 |
| QA Lead | 15 | 10 | 150 | $3,000 |
| DevOps Lead | 15 | 10 | 150 | $3,000 |
| Docs Lead | 15 | 10 | 150 | $3,000 |
| **Total** | | | **600 hrs** | **$12,000** |

### Story Point Cost Estimate (COCOMO-lite)

Total story points across backlog: **33 points**  
Average velocity: ~3–4 points/sprint  
Estimated sprints to complete: ~9–11 sprints

| Story Points | Effort Multiplier | Estimated Dev Hours |
|--------------|------------------|---------------------|
| 33 SP | 5 hrs/SP | 165 hrs |

> Story-point-based estimate is used as a cross-check against the time-based estimate above.

### Tooling & Infrastructure Cost

| Item | Cost |
|------|------|
| Development environment (VS Code, Python, Node.js) | $0 (free/open source) |
| Version control (GitHub) | $0 (free tier) |
| CI/CD pipeline (GitHub Actions) | $0 (free tier) |
| Cloud hosting (development/testing) | $0 (local/free tier) |
| **Total Tooling Cost** | **$0** |

### Total Development Cost

| Component | Cost |
|-----------|------|
| Labour (team effort) | $12,000 |
| Tooling & infrastructure | $0 |
| **Total Development Cost** | **$12,000** |

---

## 2. Operational Cost Estimation

Operational costs assume a post-launch production deployment on a minimal cloud provider (e.g., Railway, Render free tier, or AWS t3.micro).

### Annual Operational Costs

| Item | Monthly Cost | Annual Cost |
|------|-------------|-------------|
| Cloud hosting (basic VPS / free tier) | $0–$5 | $0–$60 |
| Domain name (optional) | — | $10–$15/yr |
| SSL certificate (Let's Encrypt) | $0 | $0 |
| Database (SQLite / free tier PostgreSQL) | $0 | $0 |
| Monitoring & logging tools | $0 (manual logs) | $0 |
| Maintenance (bug fixes, updates) | 2 hrs/month × $20 | $480/yr |
| **Total Annual Operational Cost** | | **~$490–$555/yr** |

---

## 3. Tangible Benefits

Tangible benefits are measurable, quantifiable gains from deploying the system.

| Benefit | Description | Estimated Annual Value |
|---------|-------------|----------------------|
| Automated user registration | Eliminates manual account creation overhead | $1,200 (saves ~5 hrs/month admin time) |
| Automated login & authentication | Replaces manual credential verification | $960 (saves ~4 hrs/month) |
| Admin user management dashboard | Reduces time to manage/remove users | $480 (saves ~2 hrs/month) |
| Centralized logging & error tracking | Faster diagnosis of system issues | $600 (saves ~2.5 hrs/month debugging) |
| Reduced manual data entry errors | Input validation prevents bad data | $300 (estimated error correction savings) |
| **Total Annual Tangible Benefits** | | **$3,540/yr** |

---

## 4. Intangible Benefits

Intangible benefits are real but harder to quantify directly.

- **Improved user experience** — Clean authentication flow reduces friction and builds trust with end users.
- **Security posture** — Input validation, `.env` secret management, and `npm audit` integration reduce exposure to data injection and credential leaks.
- **Team skill development** — Team members gain hands-on experience with Agile/Scrum, DevOps, CI/CD, and full-stack development.
- **Scalability foundation** — The modular architecture (auth, profile, admin) provides a solid base for future feature expansion without major rework.
- **Documentation culture** — Structured docs (backlog, KPIs, metrics reports, risk register) establish good engineering practices that carry forward to future projects.
- **Academic & portfolio value** — Deliverables serve as portfolio evidence of professional software development capability.
- **Stakeholder confidence** — Demonstrable KPI reporting (login success rate, error rate) provides transparency and trust in system reliability.

---

## 5. Return on Investment (ROI)

### 3-Year ROI Projection

| | Year 1 | Year 2 | Year 3 |
|-|--------|--------|--------|
| Cumulative tangible benefits | $3,540 | $7,080 | $10,620 |
| Operational costs | $530 | $530 | $530 |
| Net annual gain | $3,010 | $3,010 | $3,010 |
| **Cumulative net gain** | **$3,010** | **$6,020** | **$9,030** |

### ROI Formula

$$
\text{ROI} = \frac{\text{Net Benefit} - \text{Development Cost}}{\text{Development Cost}} \times 100
$$

**Year 1 ROI:**
```
Net Benefit (Year 1) = $3,540 - $530 = $3,010
ROI (Year 1) = ($3,010 - $12,000) / $12,000 × 100 = -74.9%
```
> Year 1 ROI is negative due to the upfront development cost — this is expected.

**Break-Even Point:**
```
Break-even = $12,000 / $3,010 per year ≈ 3.98 years
```

**3-Year Cumulative ROI:**
```
Total net gain (3 years) = $9,030
ROI (3-year) = ($9,030 - $12,000) / $12,000 × 100 = -24.75%
```

**5-Year Cumulative ROI:**
```
Total net gain (5 years) = $15,050
ROI (5-year) = ($15,050 - $12,000) / $12,000 × 100 = +25.4%
```

> The project reaches **positive ROI after approximately 4 years** of operation.

---

## 6. Recommendation

**Proceed with development and deployment.**

Although the system does not recover its full development cost within the first year, this is typical for internal tooling and academic projects where upfront investment in quality architecture yields long-term returns.

Key justifications:

1. **Zero tooling cost** keeps the total investment minimal — all infrastructure uses free-tier and open-source tools.
2. **Intangible benefits are significant** — security hardening, team skill development, and documentation culture add substantial value that is difficult to price but critical in a professional engineering context.
3. **Operational costs are very low** (~$490–$555/yr), meaning the system is inexpensive to maintain once launched.
4. **Positive ROI is achievable within 5 years**, and sooner if the system is extended with additional features that drive more user value (e.g., password reset, profile picture uploads — both already in the backlog).
5. **Risk is low** — the risk register identifies manageable risks, all with mitigation plans in place, and the modular codebase limits the blast radius of individual component failures.

> **Overall assessment:** The CS326-SIAM User Management System represents a sound investment with a clear path to positive return, strong intangible benefits, and a low operational cost profile.
