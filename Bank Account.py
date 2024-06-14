import os
from pathlib import Path
tempPath = Path(__file__).parent / 'temp'


def init():
    try:
        os.makedirs(tempPath, exist_ok=True) #Create temp directory if not exist
    except OSError:
        print(f'Temp folder creation failed, please check disk write permissions. Program will exit. ')
        return 1

class BankAccount:

    acct_type = {0: 'chequing', 1: 'savings'}
    last_acct_num = 0

    def __init__(self, name, account_type, balance=0):
        self.name = name
        self.acct_type = account_type
        self.balance = balance


        self.accountNumber = BankAccount.last_acct_num
        BankAccount.last_acct_num += 1

        self.filename = str(self.accountNumber) + "_" + BankAccount.acct_type[account_type] + "_" + self.name + ".txt"
        self.path = tempPath / self.filename

    def deposit(self, amount):
        #amount = float(input("Amount to deposit: "))
        self.balance += amount
        print("\nAmount deposited:", amount)

        # to output into a txt file
        x = open(self.path, "a")
        x.write(str(amount)+'\n')
        x.close()

    def withdraw(self, amount):
        #amount = float(input("Amount to withdraw:"))
        if amount <= self.balance:
            self.balance -= amount
            print("\nAmount withdrawn: ", amount)
        else:
            raise ValueError("\nInsufficient balance.")

        # to output into a txt file
        x = open(self.path, "a")
        x.write(str(amount)+'\n')
        x.close()

    def get_balance(self):
        return self.balance

    def get_transaction_history(self):
        x = open(self.path, "r")
        for line in x.readlines():
            print(line, end='')
        x.close()

def main():
    # print("===== Welcome! =====")
    # input_value=int(input("Enter 1 to check balance \nEnter 2 to deposit \nEnter 3 to withdraw \n Input:"))

    # Creating a new bank account
    init()
    person1 = BankAccount("Yo Gurt", 1, 1000)

    # Deposit money
    person1.deposit(300)

    # Withdraw money
    person1.withdraw(200)

    # Checking balance
    print(person1.get_balance())

    # Get transaction history
    print(person1.get_transaction_history())

    # if input_value == 1:
    # BankAccount.get_balance()
    # elif input_value == 2:
    # BankAccount.deposit()
    # elif input_value == 3:
    # BankAccount.withdraw()
    # else:
    # print("Invalid. Please Enter a valid input.")


if __name__ == "__main__":
    main()
