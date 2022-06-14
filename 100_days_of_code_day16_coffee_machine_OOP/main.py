from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
resources = CoffeeMaker()
profit = MoneyMachine()
should_continue = True

while should_continue:
    order = input(f"What would you like? {menu.get_items()}: ")

    if order == 'report':
        resources.report()
        profit.report()
    elif order == 'off':
        break
    else:
        if resources.is_resource_sufficient(menu.find_drink(order)):
            if profit.make_payment(menu.find_drink(order).cost):
                resources.make_coffee(menu.find_drink(order))
