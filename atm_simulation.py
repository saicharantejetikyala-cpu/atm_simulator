import random

def deposit():
    global balance
    n = int(input("enter the amount to deposit: "))
    balance = balance + n
    print("amount deposited!")
def withdraw():
    global balance
    k = int(input("enter the amount to withdraw: "))
    if 0 <= k <= balance:
        balance = balance - k
        print("amount withdrawn!")
    else:
        print("entered amount is not within bank balance range")
def view():
    print(f"Your Bank Balance: ${balance}")

balance = 0
while True:
    print("==============ATM=============")
    name = input("enter your name: ")
    account = input("account type(personal/professional): ")
    dob = int(input("enter your date of birth: "))
    print("generating details........")
    print(f"name:{name}\naccount:{account}\ndob:{dob}")
    rand = random.randint(1000, 9999)
    print(f"pin = {rand}")
    p = int(input("enter the pin: "))
    if p == rand:
        print("welcome to ATM!!!!\n1.deposit amount\n2.withdraw amount\n3.view bank balance\n4.quit")
        user = int(input("enter your choice: "))
        if user == 1:
            deposit()
        elif user == 2:
            withdraw()
        elif user == 3:
            view()
        elif user == 4:
            break
        else:
            print('invalid choice!!')

    else:
        print("wrong pin!!!!!")



    


