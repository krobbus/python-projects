# Guessing game (learning random and time module)

import random
import time

print("GUESS THE NUMBER")
result = random.randint(1, 20)

guess_list = []
current_guess = 0
total_guess = 5

while True:
    print(f"GUESS: {current_guess}/{total_guess}")
    guess = int(input("Enter your number (1-20): "))

    if guess > 20:
        continue
    elif guess < 1:
        continue
    else:
        current_guess += 1
        guess_list.append(guess)

        if current_guess == 5:
            count = 5

            for sec in range (count, 0, -1):
                print(sec)
                time.sleep(1)

            print(f"Your guess: {guess_list}")
            print(f"\nThe result is {result}!!!")

            if guess == result:
                print("You guessed it right!")
                break
            else:
                print("Better luck next time!")
                break