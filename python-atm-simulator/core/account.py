"""
account.py

This file handles everything related to a user's bank account.
Login, PIN verification, balance checking, and PIN change logic live here.
"""

import getpass
from database import ATM_RULES, get_user


class Account:
    """
    Account class represents a single bank account.
    It validates login and provides basic account-level operations.
    """

    def __init__(self, card_number):
        self.card_number = card_number
        self.user = get_user(card_number)
        self.failed_attempts = 0

    # -------------------------------
    # LOGIN & PIN VERIFICATION
    # -------------------------------

    def authenticate(self):
        """
        Verifies the user's PIN.
        Allows limited attempts before blocking access.
        """
        if not self.user:
            print("Invalid card number. Please contact your bank.")
            return False

        while self.failed_attempts < ATM_RULES["max_pin_attempts"]:
            pin = getpass.getpass("Enter your PIN: ")

            if pin == self.user["pin"]:
                print(f"\nWelcome, {self.user['name']}!")
                return True
            else:
                self.failed_attempts += 1
                remaining = ATM_RULES["max_pin_attempts"] - self.failed_attempts
                print(f"Wrong PIN. Attempts left: {remaining}")

        print("\nToo many wrong attempts. Account temporarily locked.")
        return False

    # -------------------------------
    # BALANCE CHECK
    # -------------------------------

    def get_balance(self):
        """
        Returns the current available balance.
        """
        return self.user["balance"]

    # -------------------------------
    # PIN CHANGE FEATURE
    # -------------------------------

    def change_pin(self):
        """
        Allows user to change PIN after verifying old PIN.
        """
        old_pin = getpass.getpass("Enter current PIN: ")

        if old_pin != self.user["pin"]:
            print("Incorrect PIN. PIN change failed.")
            return False

        new_pin = getpass.getpass("Enter new PIN: ")
        confirm_pin = getpass.getpass("Confirm new PIN: ")

        if new_pin != confirm_pin:
            print("PIN mismatch. Try again.")
            return False

        if not new_pin.isdigit() or len(new_pin) != 4:
            print("PIN must be exactly 4 digits.")
            return False

        self.user["pin"] = new_pin
        print("PIN changed successfully.")
        return True
