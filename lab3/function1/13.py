import random

def guess_the_number():
    print("Hello! What is your name?")
    name = input()
    print(f"Well, {name}, I am thinking of a number between 1 and 20.")

    secret_number = random.randint(1, 20)
    guess = 0
    num_guesses = 0

    while guess != secret_number:
        print("Take a guess.")
        guess = int(input())

        num_guesses += 1
        if guess < secret_number:
            print("Your guess is too low.")
        elif guess > secret_number:
            print("Your guess is too high.")

    print(f"Good job, {name}! You guessed my number in {num_guesses} guesses!")

guess_the_number()