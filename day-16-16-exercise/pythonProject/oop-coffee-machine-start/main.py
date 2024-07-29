from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

espresso = MenuItem("espresso", 50, 0, 18, 1.5,)
latte = MenuItem("latte", 200, 150, 24, 2.5)
cappuccino = MenuItem("cappuccino", 250, 100, 24, 3.0)

maker_of_coffee = CoffeeMaker()
money_printer = MoneyMachine()
menu_checker = Menu()

print("is available", menu_checker.get_items())
# is_on = True
# while is_on:
#     choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
#     if choice == "off":
#         is_on = False
#     elif choice == "report":
#         maker_of_coffee.report()
#         money_printer.report()

