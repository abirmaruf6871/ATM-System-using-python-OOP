"""
main.py

This is the entry point of the ATM application.
The program starts from here.
"""

from core.account import Account
from core.atm import ATM


def main():
    print("=================================")
    print("      Welcome to ATM Machine     ")
    print("=================================")

    card_number = input("Enter your card number: ").strip()

    # Create account object using card number
    account = Account(card_number)

    # Authenticate user
    if not account.authenticate():
        print("Authentication failed. Exiting system.")
        return

    # Start ATM session
    atm = ATM(account)
    atm.start()

    print("\nThank you. Have a nice day!")


if __name__ == "__main__":
    main()
