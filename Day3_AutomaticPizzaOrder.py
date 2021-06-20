# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆


#Write your code below this line 👇
# print(size)
if size == "S".lower():
  bill = 15
  if add_pepperoni == "Y".lower():
      bill += 2
  if extra_cheese == "Y".lower():
          bill += 1
          print(f"Your final bill ${bill}")
  else:
          print(f"Your final bill ${bill}")
elif size == "M":
    bill = 20
    if add_pepperoni == "Y":
      bill += 3
    if extra_cheese == "Y":
          bill += 1
          print(f"Your final bill ${bill}")
    else:
          print(f"Your final bill ${bill}")
elif size == "L":
    bill = 25
    if add_pepperoni == "Y":
      bill += 3
    if extra_cheese == "Y":
          bill += 1
          print(f"Your final bill ${bill}")
    else:
          print(f"Your final bill ${bill}")
