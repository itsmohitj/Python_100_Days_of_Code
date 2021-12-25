# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
name = name1 + name2
name = name.lower()
ten_digit = name.count('t') + name.count('r') + name.count('u') + name.count('e')
one_digit = name.count('l') + name.count('o') + name.count('v') + name.count('e')
result = (ten_digit *10) + one_digit
if result < 10 or result > 90:
    print(f"Your score is {result}, you go together like coke and mentos.")
elif result > 40 and result < 50:
    print(f"Your score is {result}, you are alright together.")
else:
    print(f"Your score is {result}.")