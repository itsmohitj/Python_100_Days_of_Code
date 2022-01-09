import art
from game_data import data
from os import system
import random

def clear():
    system('clear')

score = 0
repeat = True
print(art.logo)


first_data = random.choice(data)
second_data = random.choice(data)

while(repeat):
    second_data = random.choice(data)
    if first_data == second_data:
        second_data = random.choice(data)
    print("Compare A: " + first_data['name'] + ", " + first_data['description'] + ", from " + first_data['country'])
    print(art.vs)
    print("Compare B: " + second_data['name'] + ", " + second_data['description'] + ", from " + second_data['country'])
    answer = input("Who has more followers? Type A or B: ").upper()
    

    clear()
    print(art.logo)
    if(answer == "A" and first_data['follower_count'] > second_data['follower_count']):
        score += 1
        print(f"Correct! You current score is {score}")
        
        
    elif(answer == "B" and first_data['follower_count'] < second_data['follower_count']):
        score += 1
        print(f"Correct! You current score is {score}")
        first_data = second_data

    else:
        print(f"That is incorrect. You Lose!")
        print(f"Your final score is {score}")
        score = 0
        repeat = False