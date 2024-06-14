
class BankAccount:

    #acct_type = {0: 'chequing', 1: 'savings'}
       
    def __init__(self, name, account_type, balance=0):  
        self.name=name
        self.acct_type=account_type
        self.balance=balance
        
        def account_id():

            #generating an account ID
            import random  
            a=int(random.uniform(1,100000000))
            return a
        
        self.accountNumber=(account_id)

        self.filename = str(self.accountNumber)+"_"+self.acct_type[self.account_type]+"_"+self.name+".txt"


    def deposit(self, amount):
        amount=float(input("Amount to deposit: "))
        self.balance += amount
        print("\nAmount deposited:", amount)
        
        #to output into a txt file
        x=open(self.filename, "a")
        x.write(str(amount))
        x.close()


    def withdraw(self,amount):
        amount=float(input("Amount to withdraw:"))
        if amount <= self.balance:
            self.balance -= amount
            print("\nAmount withdrawn: ", amount)
        else:
            raise ValueError("\nInsufficient balance.")
        
        #to output into a txt file
        x=open(self.filename, "a")
        x.write(str(amount))
        x.close()


    def get_balance(self):
        return self.balance

    
    def get_transaction_history(self):
        x=open(self.filename, "r")
        output=x.read()
        print(output)
        x.close() 
        

def main():
   
    #print("===== Welcome! =====")
    #input_value=int(input("Enter 1 to check balance \nEnter 2 to deposit \nEnter 3 to withdraw \n Input:"))
    
    #Creating a new bank account
    person1 = BankAccount("Yo Gurt", 1, 1000)
    
    #Deposit money
    person1.deposit(300)

    #Withdraw money
    person1.withdraw(200)

    #Checking balance
    print(person1.get_balance)

    #Get transaction history
    #print(person_1.get_transaction_history)


    #if input_value == 1:
        #BankAccount.get_balance()
    #elif input_value == 2:
        #BankAccount.deposit()
    #elif input_value == 3:
        #BankAccount.withdraw()
    #else:
        #print("Invalid. Please Enter a valid input.")

if __name__ == "__main__":
    main()    

