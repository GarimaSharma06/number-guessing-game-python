import time
import random

print(" Hi! 😄, This is a number guessing game. 🤔\n")
time.sleep(1)
print("I have chosen a random number between 1 to 100 ")
print("Try to guess it if you can 😏")
time.sleep(1)
print("To exit the game , type '0'\n")

user_input = int(input("Enter your guess no. 1 (integer only): "))

while user_input not in range(0, 101):
    print("Enter no between 0 to 100 only\n")
    user_input = int(input("enter valid number: "))

random_no = random.randint(1, 100)

i = 1

while user_input != 0:
    if user_input > random_no:
        print("Go lower 👇\n")
    elif user_input < random_no:
        print("Go higher 👆\n")

    elif user_input == random_no:
        print("Absolutely Correct! 💯")
        print(f"The number is {random_no}")
        print(f"You guessed it in {i} attempts 😁")

        break

    i += 1
    user_input = int(input(f"Enter your guess no. {i}: "))

    while user_input not in range(0, 101):
        print("invalid input\n")
        user_input = int(input("enter valid number: "))


if user_input == 0:
    print("\nOh, sad to see you quitting.😩")
    time.sleep(1)
    print(f"The number was {random_no}")
time.sleep(0.5)
print("Hope to see you soon. 😊")
