# test_unit.py
import pytest
from bank_app import deposit, withdraw, calculate_interest, check_loan_eligibility

# ------------------
# deposit() tests
# ------------------
def test_deposit_normal():
    assert deposit(1000, 500) == 1500

def test_deposit_boundary():
    assert deposit(0, 1) == 1

def test_deposit_invalid():
    with pytest.raises(ValueError):
        deposit(1000, 0)
    with pytest.raises(ValueError):
        deposit(1000, -100)

# ------------------
# withdraw() tests
# ------------------
def test_withdraw_normal():
    assert withdraw(1000, 500) == 500

def test_withdraw_boundary():
    assert withdraw(500, 500) == 0

def test_withdraw_invalid_amount():
    with pytest.raises(ValueError):
        withdraw(1000, -50)
    with pytest.raises(ValueError):
        withdraw(1000, 0)

def test_withdraw_insufficient_balance():
    with pytest.raises(ValueError):
        withdraw(100, 200)

# ------------------
# calculate_interest() tests
# ------------------
def test_calculate_interest_normal():
    assert calculate_interest(1000, 5, 2) == 1000 * (1 + 5/100) ** 2

def test_calculate_interest_boundary():
    assert calculate_interest(0, 0, 0) == 0

def test_calculate_interest_invalid():
    with pytest.raises(ValueError):
        calculate_interest(-100, 5, 2)
    with pytest.raises(ValueError):
        calculate_interest(1000, -5, 2)

# ------------------
# check_loan_eligibility() tests
# ------------------
def test_check_loan_eligibility_true():
    assert check_loan_eligibility(6000, 750) is True

def test_check_loan_eligibility_false():
    assert check_loan_eligibility(4000, 750) is False
    assert check_loan_eligibility(6000, 650) is False

def test_check_loan_eligibility_invalid_balance():
    with pytest.raises(ValueError):
        check_loan_eligibility(-5000, 750)
