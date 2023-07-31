# Exercise: Create a Class for Bank Account Management

# Create a class called BankAccount.
# The class should have the following attributes:
# account_number (a unique identifier for each bank account).
# account_holder (the name of the account holder).
# balance (the current balance in the account).
# The class should have the following methods:
# deposit(amount): Deposits the given amount into the account.
# withdraw(amount): Withdraws the given amount from the account, if sufficient balance is available.
# get_balance(): Returns the current balance in the account.
# display_account_info(): Displays information about the account (account number, account holder, and balance).
# Test your class by creating instances of BankAccount and performing some account operations.
# Example Usage:

# python
# Copy code
# # Create a bank account instance
# account1 = BankAccount('123456789', 'John Doe', 1000.0)

# # Deposit money into the account
# account1.deposit(500.0)

# # Withdraw money from the account
# account1.withdraw(200.0)

# # Get the current balance of the account
# balance = account1.get_balance()
# print(f"Current balance: ${balance:.2f}")

# # Display account information
# account1.display_account_info()
# Expected Output:

# yaml
# Copy code
# Current balance: $1300.00
# Account Number: 123456789
# Account Holder: John Doe
# Balance: $1300.00
# In this exercise, we are creating a BankAccount class with attributes (account_number, account_holder, balance) and methods (deposit, withdraw, get_balance, display_account_info). The methods operate on the class's attributes to perform deposit and withdrawal transactions, retrieve the account balance, and display account information.

# Feel free to customize the class and add more functionalities, such as handling negative balances or providing account statements with transaction history. This exercise will give you a practical example of creating a class to manage a bank account. Happy coding and practicing!

class BankAccount:
    def __init__(self, account_number, account_holder, balance):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount:.2f} into the account.")
        else:
            print("Invalid deposit amount. Please deposit a positive amount.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount:.2f} from the account.")
        else:
            print("Insufficient funds. Withdrawal canceled.")

    def get_balance(self):
        return self.balance

    def display_account_info(self):
        print(f"Account Number: {self.account_number}")
        print(f"Account Holder: {self.account_holder}")
        print(f"Balance: {self.balance:.2f}")


# Example Usage
account1 = BankAccount('123456789', 'John Doe', 1000.0)
account1.deposit(500.0)
account1.withdraw(200.0)

balance = account1.get_balance()
print(f"Current balance: {balance:.2f}")

account1.display_account_info()
