"""
atm.py

This file controls the main ATM workflow.
It connects Account, Transaction, and Receipt together
and handles all user interactions.
"""

from database import (
    ATM_RULES,
    ATM_CASH,
    update_balance,
    add_transaction
)
from core.transaction import Transaction
from core.receipt import Receipt


class ATM:
    """
    ATM class represents the ATM machine itself.
    It shows menus, processes transactions,
    and controls the user session.
    """

    def __init__(self, account):
        self.account = account
        self.card_number = account.card_number

    # ---------------------------------
    # MAIN MENU
    # ---------------------------------

    def show_menu(self):
        print("\n===== ATM MENU =====")
        print("1. Check Balance")
        print("2. Withdraw Cash")
        print("3. Deposit Cash")
        print("4. Mini Statement")
        print("5. Change PIN")
        print("6. Exit")

    # ---------------------------------
    # START ATM SESSION
    # ---------------------------------

    def start(self):
        """
        Starts the ATM session after successful login.
        """
        while True:
            self.show_menu()
            choice = input("Select an option: ")

            if choice == "1":
                self.check_balance()

            elif choice == "2":
                self.withdraw_cash()

            elif choice == "3":
                self.deposit_cash()

            elif choice == "4":
                self.show_mini_statement()

            elif choice == "5":
                self.account.change_pin()

            elif choice == "6":
                print("Thank you for using the ATM.")
                break

            else:
                print("Invalid option. Please try again.")

            if not self.ask_another_transaction():
                print("Session ended. Please take your card.")
                break

    # ---------------------------------
    # CHECK BALANCE
    # ---------------------------------

    def check_balance(self):
        balance = self.account.get_balance()
        print(f"Your current balance is: {balance}")

        self.ask_receipt(
            transaction_type="Balance Inquiry",
            amount=0,
            balance=balance
        )

    # ---------------------------------
    # WITHDRAW CASH
    # ---------------------------------

    def withdraw_cash(self):
        try:
            amount = int(input("Enter amount to withdraw: "))
        except ValueError:
            print("Invalid amount.")
            return

        # Validate amount format
        if amount % ATM_RULES["allowed_notes"] != 0:
            print("Amount must be in multiples of 500.")
            return

        # Check daily limit
        if self.account.user["daily_withdrawn"] + amount > ATM_RULES["daily_withdraw_limit"]:
            print("Daily withdrawal limit exceeded.")
            return

        # Check account balance
        if amount + ATM_RULES["min_balance"] > self.account.get_balance():
            print("Insufficient balance.")
            return

        # Check ATM cash
        if amount > ATM_CASH["total_cash"]:
            print("ATM does not have enough cash.")
            return

        # Process withdrawal
        new_balance = self.account.get_balance() - amount
        update_balance(self.card_number, new_balance)

        self.account.user["daily_withdrawn"] += amount
        ATM_CASH["total_cash"] -= amount

        add_transaction(self.card_number, "Withdraw", amount, new_balance)

        print(f"Please collect your cash: {amount}")
        self.ask_receipt("Withdraw", amount, new_balance)

    # ---------------------------------
    # DEPOSIT CASH
    # ---------------------------------

    def deposit_cash(self):
        try:
            amount = int(input("Enter amount to deposit: "))
        except ValueError:
            print("Invalid amount.")
            return

        if amount <= 0:
            print("Deposit amount must be greater than zero.")
            return

        new_balance = self.account.get_balance() + amount
        update_balance(self.card_number, new_balance)

        add_transaction(self.card_number, "Deposit", amount, new_balance)

        print("Amount deposited successfully.")
        self.ask_receipt("Deposit", amount, new_balance)

    # ---------------------------------
    # MINI STATEMENT
    # ---------------------------------

    def show_mini_statement(self):
        transactions = self.account.user["transactions"][-5:]

        if not transactions:
            print("No transactions found.")
            return

        print("\n--- Mini Statement (Last 5 Transactions) ---")
        for txn in transactions:
            print(f"{txn['date']} | {txn['type']} | {txn['amount']} | Bal: {txn['balance']}")

    # ---------------------------------
    # RECEIPT HANDLING
    # ---------------------------------

    def ask_receipt(self, transaction_type, amount, balance):
        choice = input("Do you want a receipt? (y/n): ").lower()

        if choice == "y":
            receipt = Receipt(
                card_number=self.card_number,
                transaction_type=transaction_type,
                amount=amount,
                balance=balance
            )
            receipt.print_receipt()
            receipt.save_receipt()

    # ---------------------------------
    # ASK FOR ANOTHER TRANSACTION
    # ---------------------------------

    def ask_another_transaction(self):
        choice = input("\nDo you want another transaction? (y/n): ").lower()
        return choice == "y"
