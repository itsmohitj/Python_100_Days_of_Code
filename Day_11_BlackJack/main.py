import random
from os import system
import art
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def clear():
    system('clear')

def deal_card():
    return random.choice(cards)

def calculate_score(arr):
    score = sum(arr)
    if score == 21 and len(arr) == 2:
        return 21
    if 11 in arr and score > 21:
        arr.remove(11)
        arr.append(1)
    return score

def compare(user_score, computer_score):
    if user_score == computer_score:
        return "Tie"
    elif user_score == 0:
        return "You wins!!"
    elif computer_score == 0:
        return "You lose!! Computer wins!!"
    elif user_score > 21:
        return "You lose!! Computer wins!!"
    elif computer_score > 21:
        return "You wins!!"
    elif user_score > computer_score:
        return "You wins!!"
    else:
        return "You lose!! Computer wins!!"

def game():
    user_cards = []
    computer_cards = []
    game_over = False


    for _ in range(0,2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while(not game_over):
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        print(f"Your cards: {user_cards} and Your score: {user_score}")
        print(f"Computer's First card: {computer_cards[0]}")

        if user_score == 21 or computer_score == 21 or user_score > 21:
            game_over = True
        else:
            user_choice = input("Do you want to hit or stand? (h/s) ")
            if user_choice == "h":
                user_cards.append(deal_card())
            else:
                game_over = True

    while computer_score != 21 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"Your cards: {user_cards} and Your score: {user_score}")
    print(f"Computer's cards: {computer_cards} and Computer's score: {computer_score}")
    print(compare(user_score, computer_score))

play = True
while(play):
    clear()
    print(art.logo)
    game()
    repeat = input("Do you want to play again? (y/n) ")
    if repeat == "y":
        play = True
    else:
        play = False
        print("Bye!!!")