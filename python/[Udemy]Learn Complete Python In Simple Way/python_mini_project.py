# Define the Account class
class Account:
    # Constructor to initialize account details
    def __init__(self, name, balance, min_balance):
        self.name = name
        self.balance = balance
        self.min_balance = min_balance

    # Method to deposit funds into the account
    def deposit(self, amount):
        self.balance += amount

    # Method to withdraw funds from the account
    def withdraw(self, amount):
        if self.balance - amount >= self.min_balance:
            self.balance -= amount
        else:
            print("Sorry, Insufficient Funds")

    # Method to print the account statement
    def printStatement(self):
        print("Account Balance:", self.balance)

# Define the Current class, inheriting from Account
class Current(Account):
    # Constructor for Current Account
    def __init__(self, name, balance):
        super().__init__(name, balance, min_balance=-1000)

    # Override the __str__() method to provide a custom string representation
    def __str__(self):
        return "{}'s Current Account with Balance: {}".format(self.name, self.balance)

# Define the Savings class, inheriting from Account
class Savings(Account):
    # Constructor for Savings Account
    def __init__(self, name, balance):
        super().__init__(name, balance, min_balance=0)

    # Override the __str__() method to provide a custom string representation
    def __str__(self):
        return "{}'s Savings Account with Balance: {}".format(self.name, self.balance)

# Create a Savings account for Durga with an initial balance of 10,000
c = Savings("Durga", 10000)

# Print the account details
print(c)

# Deposit 5,000 into the account
c.deposit(5000)

# Print the account statement
c.printStatement()

# Withdraw 16,000 from the account (insufficient funds)
c.withdraw(16000)

# Attempt to withdraw 15,000 from the account
c.withdraw(15000)

# Print the updated account details
print(c)

# Create a Current account for Ravi with an initial balance of 20,000
c2 = Current('Ravi', 20000)

# Deposit 6,000 into the account
c2.deposit(6000)

# Print the account details
print(c2)

# Withdraw 27,000 from the account (insufficient funds)
c2.withdraw(27000)

# Print the updated account details
print(c2)
