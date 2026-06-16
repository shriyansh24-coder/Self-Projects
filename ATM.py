#ATM Simulator

def show_balance():
    print(f"Your balance is {balance:.2f}INR")


def deposit():
    amount = float(input("Enter the amount that has to be deposited: "))
    if amount < 0:
        print("Amount should be Grater than 0")
        return 0
    else:
        return amount
    

def withdraw():
    amount = float(input("Enter amount to be withdrawn: "))
    if amount > balance:
        print("Insufficient Funds")
        return 0
    elif amount < 0:
        print("Amount must be greater than 0")
        return 0
    else:
        return amount
    

balance = 0
is_running = True


while is_running:
    print("****Banking Program****")
    print("1.Show Balance")
    print("2.Deposit")
    print("3.Withdraw")
    print("4.Exit")

    choice = input("Enter your Choice(1-4): ")

    if choice == '1':
        show_balance()
    elif choice == '2':
        balance += deposit()
    elif choice == '3':
        balance -= withdraw()
    elif choice == '4':
        is_running = False
    else:
        print("Invalid Choice Entered")


print("Thank You! Have a Nice Day!!")