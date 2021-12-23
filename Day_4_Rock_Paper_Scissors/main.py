import random


rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''s
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

rps_dict = {1: rock, 2: paper, 3: scissors}
print("What do you choose?\n")
choice = input("Press 1 for Rock\nPress 2 for Paper\nPress 3 for Scissors\n")
computer_choice = random.randint(1, 3)
print(f"your choice: {rps_dict[int(choice)]}\nComputer choice: {rps_dict[computer_choice]}")

if(int(choice) == computer_choice):
    print("It's a tie")
elif(int(choice) == 1 and computer_choice == 2):
    print("You lose")
elif(int(choice) == 1 and computer_choice == 3):
    print("You win")
elif(int(choice) == 2 and computer_choice == 1):
    print("You win")
elif(int(choice) == 2 and computer_choice == 3):
    print("You lose")
elif(int(choice) == 3 and computer_choice == 1):
    print("You lose")
elif(int(choice) == 3 and computer_choice == 2):
    print("You win")
else:
    print("You selected an invalid option")