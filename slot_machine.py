# Slot machine program
import random

def spin():
    symbols = ["🍒", "🍌", "🍇", "🌽"]
    return [random.choice(symbols) for _ in range(3)]

def print_result(row, bet):
    if row[0] == row[1] == row[2]:
        if row[0] == "🍒":
            return bet * 2
        elif row[0] == "🍌":
            return bet * 3
        elif row[0] == "🍇":
            return bet * 5
        elif row[0] == "🌽":
            return bet * 10
    return 0

def main():
    can_play = True
    balance = 0.0

    while can_play:
        if balance <= 0:
            amount = input("Insert amount: PHP ").lower()

            if not amount.isdigit():
                print("Enter a valid number")
                continue

            amount = float(amount)

            if amount > 0:
                balance += amount
                print("Successfully inserted!")
            else:
                print("amount must be greater than 0")
                continue

        print(f"\nCurrent balance: PHP {balance:.2f}")
        bet = input("Place your bet: ")

        if not bet.isdigit():
            print("Enter a valid number")
            continue

        bet = int(bet)

        if (bet <= balance) and (bet > 0):
            balance -= bet
            row = spin()
            print(" | ".join(row))

            payout = print_result(row, bet)

            if payout > 0:
                print(f"You won {payout}!")
                balance += payout

                continue_playing = input("Do you want to continue playing (Press Q to quit)? ").lower()
                if continue_playing == "q":
                    can_play = False
            else:
                print("Sorry you loss!")
        else:
            print("Bet must be less or equal to your balance")
            continue

if __name__ == "__main__":
    print("------------------------")
    print("🍒🍌 SLOT MACHINE 🍇🌽")
    print("------------------------")
    main()
