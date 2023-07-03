def checkResources(i):
    water = drinksDict[i]["water"]
    coffee = drinksDict[i]["coffee"]
    milk = drinksDict[i]["milk"]

    if resources["water"] >= water:
        if resources["coffee"] >= coffee:
            if resources["milk"] >= milk:
                return True
            else:
                return False
        else:
            return False
    else:
        return False


def payment(index):
    """takes payment and processes coins"""
    quarters = float(input("quarters?: "))
    quarters = quarters * 0.25
    dimes = float(input("dimes?: "))
    dimes = dimes * 0.10
    nickels = float(input("nickels?: "))
    nickels = nickels * 0.05
    pennies = float(input("pennies?: "))
    pennies = pennies * 0.01
    totalGiven = quarters + dimes + nickels + pennies
    if totalGiven < drinksDict[index]["price"]:
        print("Sorry that's not enough money. Money refunded.")
    else:
        resources["money"] += drinksDict[index]["price"]
        resources["water"] -= drinksDict[index]["water"]
        resources["coffee"] -= drinksDict[index]["coffee"]
        resources["milk"] -= drinksDict[index]["milk"]

        if totalGiven > drinksDict[index]["price"]:
            change = totalGiven - drinksDict[index]["price"]
            print(f"Here is ${round(change, 2)} dollars in change.")




continueMachine = True
drinksDict = [
    {
        "name": "espresso",
        "water": 50,
        "coffee": 18,
        "milk": 0,
        "price": 1.50,
    },
    {
        "name": "latte",
        "water": 200,
        "coffee": 24,
        "milk": 150,
        "price": 2.50
    },
    {
        "name": "cappuccino",
        "water": 250,
        "coffee": 24,
        "milk": 100,
        "price": 3.00,
    }
]
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0,
}

while continueMachine:
    # prompt user
    userInput = input("What would you like? (espresso/latte/cappuccino):")
    if userInput == "report":
        for i in resources:
            print(f"{i}: {resources[i]}")
    elif userInput == "off":
        continueMachine = False
    else:
        # finds index of the drink in the list drinksDict
        index = 0
        for i in range(3):
            if drinksDict[i]["name"] == userInput:
                print(f"found at index{i}")
                index = i

        # checks if we have enough ingredients to make the drink
        if checkResources(index):
            payment(index)
            print(f"Here is your {userInput}. Enjoy!")
