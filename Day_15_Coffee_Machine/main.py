MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "milk": 0,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money" : 0
}

from os import system
def clear():
    system('clear')

def check_resources(action):
    if resources["water"] >= MENU[action]["ingredients"]["water"] and resources["milk"] >= MENU[action]["ingredients"]["milk"] and resources["coffee"] >= MENU[action]["ingredients"]["coffee"]:
        return True
    else:
        return False

def process_coins(quarters = 0, dimes = 0, nickels = 0, pennies = 0):
    monetary_value = 0
    monetary_value += quarters * 0.25
    monetary_value += dimes * 0.10
    monetary_value += nickels * 0.05
    monetary_value += pennies * 0.01
    return monetary_value

def enter_money(quarters, dimes, nickels, pennies):
    return process_coins(quarters, dimes, nickels, pennies)

def transaction(action,money):
    if money >= MENU[action]["cost"]:
        resources["water"] -= MENU[action]["ingredients"]["water"]
        resources["milk"] -= MENU[action]["ingredients"]["milk"]
        resources["coffee"] -= MENU[action]["ingredients"]["coffee"]
        resources["money"] += MENU[action]["cost"]
        return True , money - MENU[action]["cost"]
    else:
        return False

def change(action, money):
    if money > MENU[action]["cost"]:
        return money - MENU[action]["cost"]

def report():
    print(f"Water: {resources['water']} ml")
    print(f"Milk: {resources['milk']} ml")
    print(f"Coffee Beans: {resources['coffee']} g")
    print(f"Money: ${resources['money']}")

repeat = True
while(repeat):
    action = input("What would you like: espresso, latte, or cappuccino? ").lower()
    if action == "espresso" or action == "latte" or action == "cappuccino":
        if(check_resources(action)):
            quarters = int(input("Enter the number of quarters: "))
            dimes = int(input("Enter the number of dimes: "))
            nickels = int(input("Enter the number of nickels: "))
            pennies = int(input("Enter the number of pennies: "))
            if transaction(action,enter_money(quarters, dimes, nickels, pennies)):
                print("I have enough resources, making you a coffee!")
                report()
                print(f"Here is your {action}. Enjoy!")
                if change(action,enter_money(quarters, dimes, nickels, pennies)) > 0:
                    print(f"Here is your change of ${change(action,enter_money(quarters, dimes, nickels, pennies))}")
                print("Remaining resources are as follows:")
                report()
                print("Thank you!")
                print("Ready for Next Transaction")
                repeat = True
            else:
                print("Sorry, not enough money. Money refunded.")
                repeat = False
        else:
            print("Sorry, not enough resources. Please refill.")
            repeat = False
    elif action == "off":
        print("Machine is now switched off!")
        repeat = False
    elif action == "report":
        report()
        repeat = True
    else:
        print("Invalid action")
        repeat = True