"""
transaction.py

This file defines the Transaction class.
A transaction represents a single ATM operation
like withdraw, deposit, or balance inquiry.
"""

from datetime import datetime


class Transaction:
    """
    Transaction class stores information
    about a single ATM transaction.
    """

    def __init__(self, transaction_type, amount, balance):
        self.transaction_type = transaction_type
        self.amount = amount
        self.balance = balance
        self.timestamp = datetime.now()

    def get_transaction_data(self):
        """
        Returns transaction details in dictionary format.
        Useful for storing transaction history.
        """
        return {
            "type": self.transaction_type,
            "amount": self.amount,
            "date": self.timestamp.strftime("%Y-%m-%d %H:%M:%S"),
            "balance": self.balance
        }

    def display(self):
        """
        Prints transaction details in a clean format.
        Mainly useful for debugging or logging.
        """
        print(
            f"{self.timestamp.strftime('%Y-%m-%d %H:%M:%S')} | "
            f"{self.transaction_type} | "
            f"{self.amount} | "
            f"Balance: {self.balance}"
        )
