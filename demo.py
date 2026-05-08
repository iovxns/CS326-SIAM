# Demo Script — CS326-SIAM v1.0
# Run this to demonstrate the full system end-to-end

# Prerequisites: Python 3 installed
# Run from the project root: python demo.py

import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "project", "code"))

from app.user import register, login, update_profile

DIVIDER = "-" * 50

def section(title):
    print(f"\n{DIVIDER}")
    print(f"  {title}")
    print(DIVIDER)

def show(label, result):
    status = "✅ PASS" if result else "❌ FAIL"
    print(f"  {label}: {status}")

print("=" * 50)
print("  CS326-SIAM — Live Demo  (v1.0)")
print("  User Management System")
print("=" * 50)

# ── 1. Registration ──────────────────────────────────
section("1. User Registration")
show("Register 'alice' (valid)", register("alice", "securepass"))
show("Register '' empty username (should fail)", register("", "1234"))

# ── 2. Login ─────────────────────────────────────────
section("2. User Login")
show("Login 'admin' with correct password", login("admin", "1234"))
show("Login 'admin' with wrong password (should fail)", login("admin", "wrongpass"))
show("Login with empty credentials (should fail)", login("", ""))

# ── 3. Profile Update ─────────────────────────────────
section("3. Profile Update")
show("Update profile to 'Alice Johnson' (valid)", update_profile("Alice Johnson"))
show("Update profile to 'A' too short (should fail)", update_profile("A"))

# ── 4. Logging ────────────────────────────────────────
section("4. Log File Check")
log_path = os.path.join(os.path.dirname(__file__), "project", "code", "app", "app.log")
if os.path.exists(log_path):
    print(f"  ✅ app.log exists at: {log_path}")
    with open(log_path) as f:
        lines = f.readlines()
    print(f"  📋 Last 5 log entries:")
    for line in lines[-5:]:
        print(f"     {line.strip()}")
else:
    print(f"  ❌ app.log not found — run the system first.")

# ── 5. Summary ────────────────────────────────────────
print(f"\n{'=' * 50}")
print("  Demo complete.")
print("  See app.log for full audit trail.")
print("  See docs/ for architecture, KPIs, and cost-benefit analysis.")
print(f"{'=' * 50}\n")
