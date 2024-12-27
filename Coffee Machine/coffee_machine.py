#!/usr/bin/env python3
from menu import MENU, resources
from prettytable import PrettyTable

PROFIT = 0


def print_report():
    table = PrettyTable()
    table.add_column("Product", list(resources.keys()))
    table.add_column("Amount", list(resources.values()))
    table.add_column("Unit", ["ml", "ml", 'g'])
    table.align = 'l'
    print(table, f"Profit: ${PROFIT:.2f}\n", sep='\n')


def is_resources_sufficient(drink):
    ingredients = drink["ingredients"]

    for item in ingredients:
        if ingredients[item] > resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False

    return True


def insert_coins():
    total = 0
    total += float(input("Insert pennies: ")) * 0.01
    total += float(input("Insert nickles: ")) * 0.05
    total += float(input("Insert dimes: ")) * 0.1
    total += float(input("Insert quarters: ")) * 0.25

    return total


def is_transaction_successful(drink, payment):
    global PROFIT

    if payment < drink["cost"]:
        print(f"Sorry that's not enough money. Money refunded.")
        return False

    PROFIT += round(drink["cost"], 2)
    change = payment - drink["cost"]

    if change > 0:
        print(f"Here is {change:.2f} dollars in change.")

    return True


def deduct_machine_resources(drink, payment):
    ingredients = drink["ingredients"]

    for item in ingredients:
        resources[item] -= ingredients[item]


def make_coffee(order):
    drink = MENU[order]
    payment = insert_coins()

    if is_resources_sufficient(drink) and is_transaction_successful(drink, payment):
        deduct_machine_resources(drink, payment)
        print(f"Here is your {order}. Enjoy!")

def use_coffee_machine():
    machine_on = True

    while machine_on:
        order = input("What would you like? (espresso/latte/cappuccino): ")

        if order == "off":
            machine_on = False
        elif order == "report":
            print_report()
        elif order in MENU.keys():
            make_coffee(order)


if __name__ == "__main__":
    use_coffee_machine()