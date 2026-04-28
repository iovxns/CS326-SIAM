# risk register

| risk | likelihood (1-5) | impact (1-5) | score | mitigation | owner |
|------|----------------|--------------|-------|-----------|-------|
| unclear requirements | 4 | 4 | 16 | clarify with team regularly | member 1 |
| tight schedule | 3 | 5 | 15 | plan tasks weekly | member 1 |
| team member unavailable | 3 | 4 | 12 | redistribute tasks | member 2 |
| bugs in system | 4 | 4 | 16 | testing and debugging | member 3 |
| poor communication | 3 | 4 | 12 | regular meetings | member 1 |
| lack of technical skills | 2 | 4 | 8 | research and practice | member 3 |
| data loss | 2 | 5 | 10 | backup regularly | member 3 |
| scope creep | 3 | 3 | 9 | limit new features | member 4 |
| file upload errors | 3 | 3 | 9 | validate file type and size | member 3 |

Risk: Data Injection | Mitigation: Input validation.

Risk: Secret Leakage | Mitigation: Use of .env and .gitignore.

Risk: Vulnerable Packages | Mitigation: Running npm audit.