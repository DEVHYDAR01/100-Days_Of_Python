from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

espresso = MenuItem("espresso", 50, 0, 18, 1.5,)
latte = MenuItem("latte", 200, 150, 24, 2.5)
cappuccino = MenuItem("cappuccino", 250, 100, 24, 3.0)

maker_of_coffee = CoffeeMaker()
money_printer = MoneyMachine()
menu_checker = Menu()

drinks = ["espresso", "latte", "cappuccino"]

# print("is available", menu_checker.get_items())

is_on = True
while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if choice == "off":
        is_on = False
    elif choice == "report":
        maker_of_coffee.report()
        money_printer.report()
    else:
        for drink in drinks:
            if choice == drink:
                found_drink = menu_checker.find_drink(drink)
                if maker_of_coffee.is_resource_sufficient(found_drink):
                    cost_drink = found_drink.cost
                    money_printer.make_payment(cost_drink)
                    maker_of_coffee.make_coffee(found_drink)
