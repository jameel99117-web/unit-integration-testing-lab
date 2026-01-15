# test_integration.py
import pytest
from bank_app import deposit, withdraw, transfer, calculate_interest

# ------------------
# transfer() tests
# ------------------
def test_transfer_normal():
    balance_from, balance_to = transfer(1000, 500, 300)
    assert balance_from == 700
    assert balance_to == 800

def test_transfer_insufficient_balance():
    with pytest.raises(ValueError):
        transfer(100, 500, 200)

def test_transfer_invalid_amount():
    with pytest.raises(ValueError):
        transfer(1000, 500, -100)
    with pytest.raises(ValueError):
        transfer(1000, 500, 0)

# ------------------
# Combined workflow tests
# ------------------
def test_transfer_then_interest():
    # Transfer money
    balance_from, balance_to = transfer(2000, 1000, 500)
    # Apply interest on recipient balance
    balance_to_after_interest = calculate_interest(balance_to, 10, 1)
    
    assert balance_from == 1500
    assert balance_to_after_interest == 1500 * 1.10  # 10% interest for 1 year

def test_multiple_transfers():
    # Initial balances
    balance_a = 1000
    balance_b = 500
    balance_c = 200

    # Transfer from A to B
    balance_a, balance_b = transfer(balance_a, balance_b, 400)  # A->B
    # Transfer from B to C
    balance_b, balance_c = transfer(balance_b, balance_c, 300)  # B->C

    # Final balances
    assert balance_a == 600
    assert balance_b == 600
    assert balance_c == 500
