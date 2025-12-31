"""
receipt.py

This file is responsible for generating ATM receipts.
It can show the receipt on the console and also
save it as a text file for record purposes.
"""

import os
from datetime import datetime


class Receipt:
    """
    Receipt class formats and prints transaction receipts.
    """

    def __init__(self, card_number, transaction_type, amount, balance):
        self.card_number = card_number
        self.transaction_type = transaction_type
        self.amount = amount
        self.balance = balance
        self.timestamp = datetime.now()

    # ---------------------------------
    # RECEIPT CONTENT FORMAT
    # ---------------------------------

    def _build_receipt_text(self):
        """
        Creates the receipt text in ATM-style format.
        """
        return f"""
------------------------------
        ATM RECEIPT
------------------------------
Card Number   : {self.card_number}
Transaction   : {self.transaction_type}
Amount        : {self.amount}
Date & Time   : {self.timestamp.strftime('%Y-%m-%d %H:%M:%S')}
Available Bal : {self.balance}
------------------------------
Thank you for using our ATM
"""

    # ---------------------------------
    # PRINT RECEIPT ON CONSOLE
    # ---------------------------------

    def print_receipt(self):
        """
        Displays the receipt on the console.
        """
        print(self._build_receipt_text())

    # ---------------------------------
    # SAVE RECEIPT AS TEXT FILE
    # ---------------------------------

    def save_receipt(self):
        """
        Saves the receipt as a .txt file inside 'receipts' folder.
        """
        folder_name = "receipts"
        os.makedirs(folder_name, exist_ok=True)

        file_name = f"receipt_{self.card_number}_{self.timestamp.strftime('%Y%m%d_%H%M%S')}.txt"
        file_path = os.path.join(folder_name, file_name)

        with open(file_path, "w") as file:
            file.write(self._build_receipt_text())

        print(f"Receipt saved successfully: {file_path}")
