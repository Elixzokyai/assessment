
# The system will make deposit and make withdraw and return the balance.

class BankAccount:
    def __init__(self, initial_balance=0):
        self.__balance = initial_balance  # Private attribute to store balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited ${amount:.2f}. New balance: ${self.__balance:.2f}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.__balance:
                self.__balance -= amount
                print(f"Withdrew ${amount:.2f}. New balance: ${self.__balance:.2f}")
            else:
                print("Insufficient funds.")
        else:
            print("Withdrawal amount must be positive.")

    def get_balance(self):
        # Provide a way to view balance without allowing direct modification
        return self.__balance


# Demonstration
account = BankAccount(100)  # Initial balance of $100

# Deposit money
account.deposit(50)

# Withdraw money
account.withdraw(30)

# Trying to access the balance directly (not possible)
# print(account.__balance)  # This would raise an AttributeError

# Access balance safely through the method
print(f"Current balance: ${account.get_balance():.2f}")
