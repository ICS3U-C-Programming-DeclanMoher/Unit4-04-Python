#!/usr/bin/env python3
# Created by: Declan.Moher
# Created on: Nov. 15, 2023
# This program guesses a random number 0,9
import random


def main():
    random_variable = random.randint(0, 9)
    while True:
        user_guess_str = input("Enter a positve number")
        try:
            user_guess = int(user_guess_str)

        except Exception:
            print(f"{user_guess_str} is not an integer")
        else:
            if user_guess == random_variable:
                print(f"You guessed {user_guess} correctly")
                break
            elif user_guess != random_variable:
                print(f"You guessed {user_guess} incorrectly")


if __name__ == "__main__":
    main()
