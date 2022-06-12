MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
            "coffee": 18,
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

report = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0.0
}

quarter_value = 0.25
dime_value = 0.10
nickel_value = 0.05
penny_value = 0.01
should_continue = True


def coin(nominal):
    """asks user how many coins of a certain nominal he wants to pay"""
    return int(input(f"how many {nominal}?: "))


def print_report():
    """prints report of how much resources left and how much money earned"""
    print(f"Water: {report['water']}ml")
    print(f"Milk: {report['milk']}ml")
    print(f"Coffee: {report['coffee']}g")
    print(f"Money: ${report['money']}")


def calc_payment():
    """calculates total amount of money user wants to pay"""
    print("Please insert coins.")
    quarters = coin('quarters')
    dimes = coin('dimes')
    nickles = coin('nickles')
    pennies = coin('pennies')
    payment = quarters * quarter_value + dimes * dime_value + nickles * nickel_value + pennies * penny_value
    return payment


def is_resource_enough(resource):
    """checks whether it is enough resources to cook a beverage"""
    if MENU[order]['ingredients'][resource] > report[resource]:
        print(f"Sorry that is not enough {resource}.")
        return False
    else:
        return True


def is_payment_enough():
    """checks whether it is enough money to buy a beverage; updates report if yes"""
    payment = calc_payment()
    if payment >= MENU[order]['cost']:
        report['money'] += MENU[order]['cost']
        report['water'] -= MENU[order]['ingredients']['water']
        report['milk'] -= MENU[order]['ingredients']['milk']
        report['coffee'] -= MENU[order]['ingredients']['coffee']
        print(f"Here is ${round(payment - MENU[order]['cost'], 2)} in change.")
        print(f"Here is your {order}. Enjoy!")
    else:
        print("Sorry that's not enough money. Money refunded.")


while should_continue:
    order = input("  What would you like? (espresso/latte/cappuccino): ")

    if order == 'report':
        print_report()
    elif order == 'off':
        break
    else:
        if is_resource_enough('water') and is_resource_enough('milk') and is_resource_enough('coffee'):
            is_payment_enough()


# TODO Prompt user by asking “What would you like? (espresso/latte/cappuccino):”
# TODO Prompt user by asking number of coins
# TODO Turn off the Coffee Machine by entering “off” to the prompt.
# TODO When the user enters “report” to the prompt, a report should be generated that shows the current resource values.
# TODO When the user chooses a drink, the program should check if there are enough resources to make that drink.
# TODO If there are sufficient resources to make the drink selected, then the program should prompt the user to insert coins
# TODO Check that the user has inserted enough money to purchase the drink they selected.
# TODO If the transaction is successful and there are enough resources to make the drink the user selected, then the ingredients to make the drink should be deducted from the coffee machine resources.
# TODO Once all resources have been deducted, tell the user “Here is your latte. Enjoy!”