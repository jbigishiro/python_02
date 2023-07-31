# Exercise: Create a Class for Checking Account

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
# Create another class called CheckingAccount, which inherits from BankAccount.

# The CheckingAccount class should have an additional attribute:

# overdraft_limit (the maximum negative balance allowed for the checking account).
# The CheckingAccount class should override the withdraw() method from the parent class to account for the overdraft limit. If a withdrawal exceeds the available balance and is within the overdraft limit, it should be allowed, but if it exceeds the overdraft limit, it should be denied.

# The CheckingAccount class should have the following method:

# display_account_info(): Override the method from the parent class to also display the overdraft limit.
# Test your classes by creating instances of CheckingAccount, performing account operations, and checking overdraft scenarios.

# Example Usage:

# python
# Copy code
# # Create a checking account instance
# checking_account1 = CheckingAccount('987654321', 'Alice Smith', 1000.0, 500.0)

# # Deposit money into the checking account
# checking_account1.deposit(800.0)

# # Withdraw money from the checking account within the available balance
# checking_account1.withdraw(1200.0)

# # Withdraw money from the checking account exceeding the overdraft limit
# checking_account1.withdraw(500.0)

# # Get the current balance of the checking account
# balance = checking_account1.get_balance()
# print(f"Current balance: ${balance:.2f}")

# # Display checking account information
# checking_account1.display_account_info()
# Expected Output:

# javascript
# Copy code
# Deposited $800.00 into the account.
# Withdrew $1200.00 from the account.
# Withdrew $500.00 from the account.
# Current balance: $100.00
# Account Number: 987654321
# Account Holder: Alice Smith
# Balance: $100.00
# Overdraft Limit: $500.00
# In this exercise, we created two classes: BankAccount and CheckingAccount. The BankAccount class provides the basic functionality for managing a bank account, such as depositing and withdrawing funds. The CheckingAccount class inherits from BankAccount and adds an additional attribute overdraft_limit, as well as overrides the withdraw() method to handle overdraft scenarios.

# The display_account_info() method is overridden in the CheckingAccount class to add the display of the overdraft limit as well.

# The example usage demonstrates how to create an instance of CheckingAccount for an account holder named "Alice Smith" with an initial balance of $1000 and an overdraft limit of $500. We then deposit $800 and withdraw $1200 from the checking account (within the overdraft limit), and finally, we attempt to withdraw $500 (exceeding the overdraft limit) resulting in an overdraft limit denial. We display the account information including the overdraft limit.

# Feel free to further customize the classes and add more functionalities, such as implementing transaction history or handling overdraft fees. Enjoy exploring and extending the class!

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


class CheckingAccount(BankAccount):
    def __init__(self, account_number, account_holder, balance, overdraft_limit):
        super().__init__(account_number, account_holder, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if 0 < amount <= (self.balance + self.overdraft_limit):
            self.balance -= amount
            print(f"Withdrew ${amount:.2f} from the account.")
        else:
            print("Withdrawal exceeds the overdraft limit. Withdrawal canceled.")

    def display_account_info(self):
        super().display_account_info()
        print(f"Overdraft Limit: ${self.overdraft_limit:.2f}")


# Example Usage
checking_account1 = CheckingAccount('987654321', 'Alice Smith', 1000.0, 500.0)
checking_account1.deposit(800.0)
checking_account1.withdraw(1200.0)
checking_account1.withdraw(500.0)

balance = checking_account1.get_balance()
print(f"Current balance: ${balance:.2f}")

checking_account1.display_account_info()
