MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
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
money = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def check_sufficient(drink_dictionary):
    """This function will return true when is sufficient and false when is not sufficient"""
    for key in resources:
        if drink_dictionary[key] > resources[key]:
            print(f"sorry there is no enough {key}")
            return False
        return True


def coin_process():
    """This function will return the total of the coin process"""
    print("Please insert coins.")
    get_quarters = int(input("how many quarters?: ")) * 0.25
    get_dimes = int(input("how many dimes?: ")) * 0.10
    get_nickles = int(input("how many nickles?: ")) * 0.05
    get_pennies = int(input("how many pennies?: ")) * 0.01
    total = get_quarters + get_dimes + get_nickles + get_pennies
    return total


def is_transaction_successful(money_gotten, drink_cost):
    if money_gotten >= drink_cost:
        change = round(money_gotten, 2) - drink_cost
        global money
        money = money + round(money_gotten, 2)
        print(f"Here is ${change} dollars in change.")
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def make_coffee(drink_recipe):
    for key in drink_recipe:
        resources[key] = resources[key] - drink_recipe[key]
    print(f"Here is your {prefer}. ☕ Enjoy!.")


is_on = True
# TODO: 1 print report of resources
while is_on:
    prefer = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if prefer == "off":
        is_on = False
    elif prefer == 'report':
        print(f"water: {resources['water']}ml")
        print(f"milk: {resources['milk']}ml")
        print(f"coffee: {resources['coffee']}g")
        print(f"Money: ${money}")
    else:
        drink = MENU[prefer]
        if check_sufficient(drink["ingredients"]):
            coin = coin_process()
            if is_transaction_successful(coin, drink["cost"]):
                make_coffee(drink["ingredients"])
# TODO: 2 check resource sufficient

# TODO: 3 process coins

# TODO: 4 make coffe
