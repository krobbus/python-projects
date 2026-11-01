# Python bank program

def show_balance(balance):
    print("\n" * 2)
    print("----- Bank Program -----")
    print(f"Your current balance: PHP {balance:.2f}")
    print("[0] Go Back")
    print("------------------------")

    while True:
        try:
            action = int(input("\nInput [0] to go back: "))
            if action == 0:
                break
            else:
                print("Not valid action. Try again.")
        except ValueError:
            print("Please enter a valid number.")

def deposit(balance):
    print("\n" * 2)
    print("----- Bank Program -----")
    print(f"Your current balance: PHP {balance:.2f}")
    print("[0] Go Back")
    print("------------------------")

    while True:
        try:
            amount = float(input("\nEnter an amount to be deposited (or 0 to go back): "))
            if amount < 0:
                print("Not valid amount. Try again.")
            else:
                return amount
        except ValueError:
            print("Please enter a valid number.")

def withdraw(balance):
    print("\n" * 2)
    print("----- Bank Program -----")
    print(f"Your current balance: PHP {balance:.2f}")
    print("[0] Go Back")
    print("------------------------")

    while True:
        try:
            amount = float(input("\nEnter an amount to be withdrawn (or 0 to go back): "))
            if amount < 0:
                print("Amount must be greater than or equal to 0. Try again.")
            elif amount > balance:
                print("Insufficient funds. Try again.")
            else:
                return amount
        except ValueError:
            print("Please enter a valid number.")

def main():
    balance = 0.0
    is_running = True

    while is_running:
        print("\n" * 2)
        print("----- Bank Program -----")
        print("[0] Show Balance")
        print("[1] Deposit")
        print("[2] Withdraw")
        print("[3] Exit program")
        print("------------------------")

        try:
            action = int(input("\nSelect action (input 0-3): "))

            if action == 0:
                show_balance(balance)
            elif action == 1:
                balance += deposit(balance)
            elif action == 2:
                balance -= withdraw(balance)
            elif action == 3:
                is_running = False
            else:
                print("Not valid action. Please choose between 0 and 3.")
        except ValueError:
            print("Invalid input! Please enter a number between 0 and 3.")

    print("\nThank you for using the bank program. Have a nice day!")

if __name__ == "__main__":
    main()