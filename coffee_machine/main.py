from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()
is_on = True

while is_on:
    options = menu.get_items()
    choice = input(f"What would you like? ({options}): ")
    if choice == "off":
        is_on = False
    # Print reports.
    elif choice == "report":
        money_machine.report()
        coffee_maker.report()
    else:
        drink = menu.find_drink(choice)
        # Check whether the resources are sufficient and the transaction is successful?
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)


# ----------------------------- OUTPUT -----------------------------

# What would you like? (latte/espresso/cappuccino/): report
# Money: $0
# Water: 300ml
# Milk: 200ml
# Coffee: 100g

# What would you like? (latte/espresso/cappuccino/): cappuccino
# Please insert coins.
# How many quarters?: 1
# How many dimes?: 1
# How many nickles?: 1
# How many pennies?: 1
# Sorry that's not enough money. Money refunded.

# What would you like? (latte/espresso/cappuccino/): cappuccino
# Please insert coins.
# How many quarters?: 15
# How many dimes?: 10
# How many nickles?: 10
# How many pennies?: 10
# Here is $2.35 in change.
# Here is your cappuccino ☕️. Enjoy!

# What would you like? (latte/espresso/cappuccino/): cappuccino
# Sorry there is not enough water.

# What would you like? (latte/espresso/cappuccino/): espresso
# Please insert coins.
# How many quarters?: 15
# How many dimes?: 5
# How many nickles?: 5
# How many pennies?: 5
# Here is $3.05 in change.
# Here is your espresso ☕️. Enjoy!

# What would you like? (latte/espresso/cappuccino/): report
# Money: $4.5
# Water: 0ml
# Milk: 150ml
# Coffee: 58g
# What would you like? (latte/espresso/cappuccino/): off

