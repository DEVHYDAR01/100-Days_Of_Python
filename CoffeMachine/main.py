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


def report(resource):
    """This function will take in the resource and print the report"""
    for key in resources:
        get_key = key
        get_value = resources[key]
        print(f"{get_key}: {get_value}")


def cost_update():
    """This function will print cost of the cost dict for now"""
    for key in cost:
        get_key = key
        get_value = cost[key]
        return f"{get_key}: {get_value}"


def get_drink_recipe(menu):
    get_ingredients = MENU[prefer]
    recipe = get_ingredients["ingredients"]
    return recipe


def get_drink_recipe_keys(recipe):
    get_water = drink_recipe["water"]
    if "milk" in drink_recipe:
        get_milk = drink_recipe["milk"]
    else:
        get_milk = 0
    get_coffee = drink_recipe["coffee"]
    return f"water is {get_water} milk is {get_milk} coffee is {get_coffee}"


# # TODO: 1 print report of resources
prefer = input("What would you like? (espresso/latte/cappuccino): ").lower()
if prefer == "report":
    report(resources)
    update_money = cost_update()
    print(update_money)
elif prefer == "espresso":
    drink_recipe = get_drink_recipe(MENU)
    print(drink_recipe)
    recipe_keys = get_drink_recipe_keys(drink_recipe)
    print(recipe_keys)

elif prefer == "latte":
    drink_recipe = get_drink_recipe(MENU)
    print(drink_recipe)
    recipe_keys = get_drink_recipe_keys(drink_recipe)
    print(recipe_keys)

# elif prefer == "cappuccino":

# elif prefer == "off":


# TODO: 2 check resource sufficient

# TODO: 3 process coins

# TODO: 4 make coffe
