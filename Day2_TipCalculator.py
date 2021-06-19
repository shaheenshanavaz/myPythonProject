print("Welcome to the tip  calculator.")
tot_bill = input("What was the total bill?")
tips = input("What percentage tip you like to give 10,12 or 15?")
people = input("How many people to split the bill?")
tip_calc = 1 + float(tips)/100
# print(type(tip_calc))
each_person_bill = float(tot_bill) / int(people) * tip_calc
print(f"Each person should pay: {round(each_person_bill,2)}")