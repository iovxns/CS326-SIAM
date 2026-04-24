import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.user import register, login, update_profile

def test_register_success():
    assert register("john", "1234") == True


def test_register_fail_empty():
    assert register("", "1234") == False


def test_login_success():
    assert login("admin", "1234") == True


def test_login_fail():
    assert login("admin", "wrong") == False


def test_update_profile_valid():
    assert update_profile("john") == True