# Exercise: Create a Class for Savings Account

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
# Create another class called SavingsAccount, which inherits from BankAccount.

# The SavingsAccount class should have an additional attribute:

# interest_rate (the interest rate for the savings account).
# The SavingsAccount class should have the following method:

# calculate_interest(): Calculates and returns the interest earned on the savings account balance.
# Override the display_account_info() method from the parent class to also display the interest rate.
# Test your classes by creating instances of SavingsAccount, performing account operations, and calculating the interest earned.

# Example Usage:

# python
# Copy code
# # Create a savings account instance
# savings_account1 = SavingsAccount('987654321', 'Jane Doe', 2000.0, 0.05)

# # Deposit money into the savings account
# savings_account1.deposit(1000.0)

# # Withdraw money from the savings account
# savings_account1.withdraw(500.0)

# # Get the current balance of the savings account
# balance = savings_account1.get_balance()
# print(f"Current balance: ${balance:.2f}")

# # Calculate the interest earned on the savings account
# interest_earned = savings_account1.calculate_interest()
# print(f"Interest earned: ${interest_earned:.2f}")

# # Display savings account information
# savings_account1.display_account_info()
# Expected Output:

# javascript
# Copy code
# Deposited $1000.00 into the account.
# Withdrew $500.00 from the account.
# Current balance: $2500.00
# Interest earned: $125.00
# Account Number: 987654321
# Account Holder: Jane Doe
# Balance: $2500.00
# Interest Rate: 0.05
# In this exercise, we created two classes: BankAccount and SavingsAccount. The BankAccount class provides the basic functionality for managing a bank account, such as depositing and withdrawing funds. The SavingsAccount class inherits from BankAccount and adds the functionality to calculate and display interest earned on the savings account.

# Feel free to customize the classes and add more functionalities to further enhance the Bank Account management system. For example, you could add methods to handle account transfers, implement a checking account class, or provide a summary of the account's transaction history. Happy coding and practicing!


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
        print(f"Balance: ${self.balance:.2f}")


class SavingsAccount(BankAccount):
    def __init__(self, account_number, account_holder, balance, interest_rate):
        super().__init__(account_number, account_holder, balance)
        self.interest_rate = interest_rate

    def calculate_interest(self):
        return self.balance * self.interest_rate

    def display_account_info(self):
        super().display_account_info()
        print(f"Interest Rate: {self.interest_rate:.2%}")


# Example Usage
savings_account1 = SavingsAccount('987654321', 'Jane Doe', 2000.0, 0.05)
savings_account1.deposit(1000.0)
savings_account1.withdraw(500.0)

balance = savings_account1.get_balance()
print(f"Current balance: ${balance:.2f}")

interest_earned = savings_account1.calculate_interest()
print(f"Interest earned: ${interest_earned:.2f}")

savings_account1.display_account_info()
