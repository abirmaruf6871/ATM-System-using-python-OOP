"""
database.py

This file acts as the temporary data storage for the ATM system.
No external database is used.
All users, ATM rules, and transaction records live here.
"""

from datetime import datetime

# ---------------------------------
# ATM RULES AND LIMITATIONS
# ---------------------------------
# These rules control how the ATM behaves.
# If you want to change limits later, just update values here.

ATM_RULES = {
    "daily_withdraw_limit": 20000,   # Maximum amount a user can withdraw per day
    "min_balance": 500,              # Minimum balance that must remain in account
    "allowed_notes": 500,            # Withdraw amount must be multiple of 500
    "max_pin_attempts": 3            # Maximum wrong PIN attempts allowed
}

# ---------------------------------
# TOTAL CASH AVAILABLE IN ATM
# ---------------------------------
# This represents how much money the ATM currently has.
# If ATM cash becomes low, withdrawals should be blocked.

ATM_CASH = {
    "total_cash": 100000
}

# ---------------------------------
# USER DATA STORAGE
# ---------------------------------
# Each user is identified by a card number.
# Data includes PIN, balance, daily withdrawal tracking,
# and transaction history.

USERS = {
    "1234567890": {
        "name": "Abdullah Al Maruf",
        "pin": "1234",
        "balance": 25000,
        "daily_withdrawn": 0,
        "transactions": [
            {
                "type": "Deposit",
                "amount": 5000,
                "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "balance": 25000
            }
        ]
    },

    "9876543210": {
        "name": "Demo User",
        "pin": "4321",
        "balance": 15000,
        "daily_withdrawn": 0,
        "transactions": []
    }
}

# ---------------------------------
# HELPER FUNCTIONS
# ---------------------------------
# These functions are used by other files
# to read or update user data safely.


def get_user(card_number):
    """
    Returns user information if the card number exists.
    If not found, returns None.
    """
    return USERS.get(card_number)


def update_balance(card_number, new_balance):
    """
    Updates the user's account balance after a transaction.
    """
    USERS[card_number]["balance"] = new_balance


def add_transaction(card_number, transaction_type, amount, balance):
    """
    Saves a transaction record for mini statement and receipt.
    """
    USERS[card_number]["transactions"].append({
        "type": transaction_type,
        "amount": amount,
        "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "balance": balance
    })


def reset_daily_withdraw(card_number):
    """
    Resets daily withdrawn amount.
    Useful when a new day starts.
    """
    USERS[card_number]["daily_withdrawn"] = 0
