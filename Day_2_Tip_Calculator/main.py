print("Welcome to the Tip Calculator!")
bill = float(input("What is the total bill? "))
tip = float(input("How much tip in precentage do you want to give? "))
people = int(input("How many people are splitting the bill? "))

tip_amount = bill * (tip/100)
total_bill = bill + tip_amount
bill_per_person = total_bill / people

print("The total bill is ${:.2f}".format(total_bill))
print("The tip amount is ${:.2f}".format(tip_amount))
print("Each person should pay ${:.2f}".format(bill_per_person))
