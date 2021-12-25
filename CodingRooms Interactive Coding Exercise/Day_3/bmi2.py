# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
bmi = round(weight / (height**2))

bmi_answer = ["underweight", "normal weight", "slightly overweight", "obese", "clinically obese"]

if bmi<18.5:
    print(f"Your BMI is {bmi}, you are {bmi_answer[0]}.")
elif bmi<25:
    print(f"Your BMI is {bmi}, you have a {bmi_answer[1]}.")
elif bmi<30:
    print(f"Your BMI is {bmi}, you are {bmi_answer[2]}.")
elif bmi<35:
    print(f"Your BMI is {bmi}, you are {bmi_answer[3]}.")
else:
    print(f"Your BMI is {bmi}, you are {bmi_answer[4]}.")    