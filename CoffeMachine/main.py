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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

money = 0


def check_sufficient(drink_dictionary):
    for key in resources:
        if drink_dictionary[key] > resources[key]:
            print(f"sorry there is no enough {key}")
            return False
        return True

def coin_process():


is_on = True
# TODO: 1 print report of resources
while is_on:
    prefer = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if prefer == "off":
        is_on = False
    elif prefer == 'report':
        get_money = money
        print(f"water: {resources['water']}ml")
        print(f"milk: {resources['milk']}ml")
        print(f"coffee: {resources['coffee']}g")
        print(f"Money: ${money}")
    else:
        drink = MENU[prefer]
        print(drink)
        suffice = check_sufficient(drink["ingredients"])
        print(suffice)


# TODO: 2 check resource sufficient

# TODO: 3 process coins

# TODO: 4 make coffe
