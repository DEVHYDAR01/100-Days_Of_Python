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
cost = {"money": 0}


# # TODO: 1 print report of resources
def report():
    water_report = resources["water"]
    milk_report = resources["milk"]
    coffe_report = resources["coffee"]
    print(f"water: {water_report}")
    print(f"milk: {milk_report}")
    print(f"water: {coffe_report}")


def recipe():
    ingredient = MENU[prefer]["ingredients"]
    return ingredient


prefer = input("What would you like? (espresso/latte/cappuccino): ").lower()
ingredients = recipe()



# report()

# TODO: 2 check resource sufficient

# TODO: 3 process coins

# TODO: 4 make coffe
