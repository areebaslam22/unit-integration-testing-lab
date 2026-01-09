import pytest
from bank_app import deposit, withdraw, calculate_interest, check_loan_eligibility

def test_deposit_valid():
    assert deposit(1000, 500) == 1500

def test_deposit_invalid():
    with pytest.raises(ValueError):
        deposit(1000, -100)

def test_withdraw_valid():
    assert withdraw(1000, 500) == 500

def test_withdraw_invalid():
    with pytest.raises(ValueError):
        withdraw(1000, 1500)

def test_calculate_interest():
    assert calculate_interest(1000, 10, 2) == pytest.approx(1210.0)


def test_check_loan_eligibility_true():
    assert check_loan_eligibility(6000, 750) == True

def test_check_loan_eligibility_false():
    assert check_loan_eligibility(4000, 650) == False
