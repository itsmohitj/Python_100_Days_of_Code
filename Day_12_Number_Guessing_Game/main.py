print("Welcome to the Number Guessing Game!")
print("Guess a number between 1 and 100.")
print("If you guess the number, you win!")
print("If you don't, you lose!")
print("Good luck!")

import art
import random
print(art.logo)


number = random.randint(1, 100)
number_of_guesses = 0
difficulty_level = ["easy", "medium", "hard"]
difficulty = input("Choose a difficulty level: Easy, Medium, or Hard: ")
difficulty = difficulty.lower()
if difficulty == "easy":
    number_of_guesses = 10
elif difficulty == "medium":
    number_of_guesses = 5
else:
    number_of_guesses = 3

while(number_of_guesses > 0):
    guess = int(input("Guess a number: "))
    number_of_guesses -= 1
    if guess == number:
        print("You win!")
        break
    else:
        if guess > number:
            print("Your guess is too high!")
        else:
            print("Your guess is too low!")
        print(f"You have {number_of_guesses} guesses left.")

if(number_of_guesses == 0):
    print("You lose!!!")
    print(f"The number was {number}")
