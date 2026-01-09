import pytest
from bank_app import deposit, withdraw, transfer, calculate_interest

def test_transfer_valid():
    bal_from, bal_to = transfer(1000, 500, 300)
    assert bal_from == 700
    assert bal_to == 800

def test_transfer_insufficient_balance():
    with pytest.raises(ValueError):
        transfer(200, 500, 300)
def test_transfer_with_interest():
    bal_from, bal_to = transfer(1000, 500, 500)
    bal_to_interest = calculate_interest(bal_to, 10, 1)
    assert bal_to_interest == 1100.0


