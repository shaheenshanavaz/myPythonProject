from main import resources,MENU

def reportfunc():
    #  resources["Money"] = profit
     return resources

def reportfuncwithmoney(profit):
    resources["Money"] += profit
    return resources


# TODO 1: Resources sufficient
def resources_sufficient(resources,coffee):
    dict2 = MENU[coffee]["ingredients"]
    if coffee == "latte" or coffee == "cappuccino":
        for key in resources:
            if key == "Money":
                continue
            elif resources[key] < dict2[key]:
                print(f"Sorry ,there is no enough {key}")
    elif coffee == "espresso":
        for key in resources:
            if key == "milk" or key == "Money":
                continue
            elif resources[key] < dict2[key]:
                print(f"Sorry ,there is no enough {key}")
    # print(f"Please enjoy your {coffee}")
    return True  


# TODO 2: Check Coins
def amount_calculation(calculate_total,coffee):
    dict2 = MENU[coffee]["cost"]
    if calculate_total < dict2:
        print("Sorry that's not enough money. Money refunded.")
    else:
        change = calculate_total - dict2
        print(dict2)
        added = reportfuncwithmoney(dict2)
        print(added)
        print(f"Please enjoy your {coffee} and your change is {change}")


def report_update(resources,coffee):
    dict = MENU[coffee]["ingredients"]
    # resources[key] - dict[key]
    if coffee == "latte" or coffee == "cappuccino":
        for key in resources:
            if key == "Money":
                continue
            else:
                resources[key] = resources[key] - dict[key]
            return resources
    elif coffee == "espresso":
        for key in resources:
            if key == "milk" or key == "Money":
                continue
            else:
                resources[key] = resources[key] - dict[key]
    return resources


profit = 0
resources["Money"] = profit
coffee_machine_ended = False

while not coffee_machine_ended:
    coffee_choice = input("What would you like? (espresso/latte/cappuccino):").lower()
    if coffee_choice == "off":
        coffee_machine_ended = True
    
    elif coffee_choice == "report":
        for key, value in reportfunc().items():
            print(f"{str(key).capitalize()} : {value}")

    elif coffee_choice == "espresso" or "latte" or "cappuccino":
        check_resources = resources_sufficient(reportfunc(),coffee_choice)
        if check_resources:
            # report_update(reportfunc(),coffee_choice)
            print("Please enter your coins\n")
            quarter = int(input("How many quarters:"))
            nickles = int(input("How many nickles:"))
            pennies = int(input("How many pennies:"))
            dimes = int(input("How many dimes:"))
            calculate_total = (0.25 * quarter + 0.05 * nickles + 0.01 * pennies + 0.10 * dimes)
            amount_calculation(calculate_total,coffee_choice)
            ingredients_report = report_update(reportfunc(),coffee_choice)



    






