import sys

class Customer:
    '''Customer class with bank operations..'''
    bankname = 'NakBANK'  # Class variable to store the bank name

    def __init__(self, name, balance=0.0):
        self.name = name
        self.balance = balance  # Instance variable to store the account balance

    def deposit(self, amt):
        if amt <= 0:
            print('Deposit amount should be greater than 0.')
            return
        self.balance += amt  # Increase balance by the deposited amount
        print('Balance after deposit:', self.balance)

    def withdraw(self, amt):
        if amt <= 0:
            print('Withdrawal amount should be greater than 0.')
            return
        if amt > self.balance:
            print('Insufficient Funds..cannot perform this operation')
            return
        self.balance -= amt  # Decrease balance by the withdrawn amount
        print('Balance after withdrawal:', self.balance)

print('Welcome to', Customer.bankname)
name = input('Enter Your Name:').strip()

while not name:
    print('Name cannot be empty. Please enter your name.')
    name = input('Enter Your Name:').strip()

initial_balance = 0.0
while True:
    try:
        initial_balance = float(input('Enter Initial Balance (0 for default):'))
        break
    except ValueError:
        print('Invalid input. Please enter a valid initial balance.')

c = Customer(name, initial_balance)

while True:
    print('\nd-Deposit \nw-Withdraw \ne-Exit')
    option = input('Choose your option:').strip().lower()

    if option == 'd':
        try:
            amt = float(input('Enter deposit amount:'))
            c.deposit(amt)
        except ValueError:
            print('Invalid input. Please enter a valid amount.')
    elif option == 'w':
        try:
            amt = float(input('Enter withdrawal amount:'))
            c.withdraw(amt)
        except ValueError:
            print('Invalid input. Please enter a valid amount.')
    elif option == 'e':
        print('Thanks for Banking')
        sys.exit()  # Exit the program
    else:
        print('Invalid option. Please choose a valid option.')
