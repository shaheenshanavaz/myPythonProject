rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
import random

game_images = [rock,paper,scissors]
ur_choice = input("what do u choose 0 for rock, 1 for paper, and 2 for scissors:\n")
print(game_images[int(ur_choice)])

comp_choice = str(random.randint(0,2))
print(f"computer choose:\n")
print(game_images[int(comp_choice)])

if(ur_choice == comp_choice):
  print("Its a draw")

mywin = ["02","10","21"]

for i in mywin:
  combination = i
  pos1 = combination[0]
  pos2 = combination[1]
  if ur_choice == pos1 and comp_choice == pos2:
    print("You win")
  
# print("computer wins")
compwin = ["01","12","20"]

for i in compwin:
  combination = i
  pos1 = combination[0]
  pos2 = combination[1]
  if ur_choice == pos1 and comp_choice == pos2:
    print("Computer wins")




