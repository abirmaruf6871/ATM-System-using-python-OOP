# Python ATM Simulator (OOP Based)

A console-based ATM Machine simulation built using Python and Object-Oriented Programming (OOP) principles.  
This project does not use any external database. All data is handled through Python files to keep the system simple, readable, and focused on core logic.

---

## 🔹 Project Overview

This project simulates the real-life behavior of an ATM machine including authentication, transactions, security rules, and receipt generation.  
It is designed with clean OOP architecture where each component has a clear responsibility.

This project is suitable for:

- Learning Python OOP with a real-world use case
- Academic and lab projects
- Interview preparation
- GitHub portfolio showcase

---

## 🔹 Features

### Core ATM Features

- User authentication using Card Number / User ID and PIN
- Balance inquiry
- Cash withdrawal
- Cash deposit
- Safe logout system

### Real ATM Inspired Features

- Fast cash option (predefined amounts)
- PIN change functionality
- Mini statement (last few transactions)
- Daily withdrawal limit
- ATM cash availability check
- Amount validation (only multiples of 500 allowed)
- Option to perform another transaction or logout

### Receipt System

- Transaction receipt generation
- User can choose whether to print a receipt or not
- Receipt includes:
  - Card number
  - Transaction type
  - Amount
  - Date and time
  - Available balance
- Receipt can be displayed in console
- Optional receipt saved as a text file

### Security & Validation

- PIN verification with limited attempts
- Insufficient balance protection
- Invalid input handling
- Unknown card detection

---

## 🔹 Project Structure

```text
python-atm-simulator/
│
├── core/
│   ├── __init__.py
│   ├── account.py        # Account-related logic
│   ├── atm.py            # ATM operations and user flow
│   ├── transaction.py   # Transaction handling
│   └── receipt.py       # Receipt generation logic
│
├── database.py           # User and ATM data stored as Python structures
├── main.py               # Program entry point
├── requirements.txt
└── README.md
```
