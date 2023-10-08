import random
import datetime

class BankApp:
    bank_name = "AXIS"
    branch = "Vasna-Bhayali"
    IFSC = "Axis0003"
	
    def __init__(self, cname, pin, balance = 5000):
        self.customer_id = random.randint(111111,999999)
        self.account_no = random.randint(111111111,999999999)
        self.customer_name = cname
        self.pin = pin
        self.balance = balance

    def get_customer_details(self):
        print(f'''Customer ID: {self.customer_id}
	Customer Account Number: {self.account_no}
	Customer Name: {self.customer_name}
	Bank Balance: {self.balance}''')

    def get_branch_details(cls):
        print(f'''Bank Name: {cls.bank_name}
	Branch: {cls.branch}
	IFSC: {cls.IFSC}''')

    def get_balance(self):
        print(f'''The account balance is {self.balance} on {datetime.datetime.now()}''')

    def deposit(self, amt):
        self.balance += amt
        print(f'''The amount {amt} is successfully deposited to the account''')
        B1.get_balance()

    def withdraw(self,amt):
        if amt > self.balance:
            print("Insufficient Balance")
        else:
            self.balance -= amt
            print(f'''The amount {amt} is successfully deducted from your amount''')
            B1.get_balance()

    def get_loan(self, amt):
        if amt > self.balance*10:
            print("You are not eligible for amount  {amt}. You can get loan upto {self.balance*10}")
        elif self.balance < 10000:
            print("Insufficient account balance to apply for loan")
        else:
            self.balance += amt
            print("Congratulations, your loan has been approved, it is in process. The loan amount will be added to your account shortly.")
			
print("Welcome to AXIS Bank")
user_name = input("Enter the customer name: ")
pin = input("Enter the pin: ")
B1 = BankApp(user_name, pin)
count = 0
while True:
    print("How can we help you")
    print(
    f'''
    B - Balance
    C - Customer Details
    G - Branch Details
    D - Deposit
    W - Withdraw
    L - Loan
    E - Exit''')
    user_inp = input("Select any option: ").upper()

    if user_inp == "B":
        B1.get_balance()
    elif user_inp == "C":
        B1.get_customer_details()
    elif user_inp == "G":
        B1.get_branch_details()
    elif user_inp == "D":
        amount = int(input("Enter the amount to be deposited: "))
        B1.deposit(amount)
    elif user_inp == "W":
        amount = int(input("Enter the amount to be withdrawn: "))
        B1.withdraw(amount)
    elif user_inp == "L":
        amount = int(input("Enter the loan amount: "))
        B1.get_loan(amount)
    elif user_inp == "E":
        print("Thank you for banking with us")
        break
    else:
        print("invalid Option")
        count += 1
        if count == 3:
            break

    user_option = input("Do you want to continue? Yes/No ").upper()
    if user_option in ("YES","Y"):
        continue
    else:
        print("Thank you for banking with us")
        break
    break 
