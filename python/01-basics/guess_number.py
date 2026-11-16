import random

random_number = random.randint(1, 100)
attempts = 7

#print(random_number)

while True:
    user_number = int(input("Guess the number: "))

    if user_number == random_number:
        print("You guessed the number")
        break

    attempts -= 1

    if attempts == 0:
        print(f"Game Over. Guessed is number {random_number}")
        break


    if user_number > random_number:
        print(f"Too high. Attempts: {attempts}")
    else:
        print(f"Too low. Attempts: {attempts}")