# Simple ATM Program

# Initial details
pin =1234
balance = 5000

print("==== Welcome to Python ATM ====")

# PIN verification
entered_pin = int(input("Enter your PIN: "))

if entered_pin == pin:
    while True:
        print("\n ---- ATM Menu ----")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")

        choice = int(input("Enter your choice (1-4): "))

        if choice == 1:
            print(f"Your current balance is : ${balance}")
        
        elif choice == 2:
            deposit = int(input("Enter amount to deposit: $"))
            if deposit > 0:
                balance += deposit
                print(f"${deposit} Deposited Successfully")
            else:
                print("Invalid Deposit Amount")
        
        elif choice == 3:
            withdraw = int(input("Enter amount to withdraw: $"))
            if withdraw > 0 and withdraw <= balance:
                balance -= withdraw
                print(f"${withdraw} Withdrawn Successfully")
            else:
                print("Invalid Withdrawal Amount or Insufficient Balance")
        
        elif choice == 4:
            print("Thank you for using Python ATM. Goodbye!")
            break

        else:
            print("Invalid Choice. Please select a valid option.")
else:
    print("Incorrect PIN. Access Denied.")