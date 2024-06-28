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


def report(resource):
    for key in resources:
        get_key = key
        get_value = resources[key]
        print(f"{get_key}: {get_value}")


# TODO: 1 print report of resources
prefer = input("What would you like? (espresso/latte/cappuccino): ").lower()
if prefer == "report":
    report(resources)



# TODO: 2 check resource sufficient

# TODO: 3 process coins

# TODO: 4 make coffe
