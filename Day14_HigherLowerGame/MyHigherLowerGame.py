import random
from game_data import data
import art
# from replit import clear

def func():
  data_length = len(data)
  n = random.randint(0,data_length-1)
  item = data[n]
  # return item['follower_count']
  return item['name'], item['description'], item['country'],item['follower_count']

# def swap_func():
#   a_name=b_name
#   a_description = b_description
#   a_country = b_country
#   b_name,b_description,b_country,b_follower_count = func() 

  

a_name,a_description,a_country,a_follower_count = func()
b_name,b_description,b_country,b_follower_count = func()

is_game_ended = False
points = 0

while not is_game_ended:
  print(f"Compare A: {a_name} a {a_description} from {a_country}")
  print(f"Against B: {b_name} a {b_description} from {b_country}")

  choose = input("Who has more followers 'A' or 'B'").lower()
  
  if (choose == 'a'and a_follower_count > b_follower_count) or (choose == 'b' and b_follower_count > a_follower_count):
    points =  points + 1
    a_name=b_name
    a_description = b_description
    a_country = b_country
    b_name,b_description,b_country,b_follower_count = func()
    # clear()
    print(f"You're right! Current score: {points}.")
  
    # else:
    #   print(f"Sorry your wrong.Your score is {points}")
    #   is_game_ended = True
  # elif choose == 'b' and b_follower_count > a_follower_count:
  #   points =  points + 1
  #   a_name=b_name
  #   a_description = b_description
  #   a_country = b_country
  #   b_name,b_description,b_country,b_follower_count = func()
  #   clear()
  #   print(f"You're right! Current score: {points}.")
    # else:
    #   print(f"Sorry your wrong.Your score is {points}")
    #   is_game_ended = True
  else:
    print(f"Sorry your wrong.Your score is {points}")
    is_game_ended = True


 
