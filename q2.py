# creating a class and object program with class name as BankAccount 

# class defination
class BankAccount():

    def __init__(self,acc_no,acc_hold,bal): # init method
        # instance variable
        self.account_number=acc_no
        self.account_holder=acc_hold
        self.balance=bal

    def deposit(self,money): # deposit function

        self.balance += money # calculation
        print(f"The money added= ",money)
        print("The Total Balance in Account= ",self.get_balance())

    def withdraw(self,money): # withdraw function
        if money > self.balance: # enquirying the balance amount
            print("Insufficent amount is withdrawn")
        else:
            self.balance -= money # calculation
            print(f"The money subtraced from current account= ",money)
        print("The Total Balance in Account= ",self.get_balance())

    def get_balance(self): # balance function
        return self.balance

# user input    
acc_no=input("Enter the account number: ")
acc_holder=input("Enter the account holder: ")
bal=float(input("Enter the amount present in account:"))

# object declaration
first_account=BankAccount(acc_no,acc_holder,bal)

# displaying the account number,account holder name, amount in account
print(first_account.account_number)
print(first_account.account_holder)
print("The inital amount:",first_account.balance)

first_account.deposit(float(input("Enter the amount to be deposited in bank account: "))) # deposit function call

first_account.withdraw(float(input("Enter the amount to be withdrawn from the account: "))) # withdraw function call