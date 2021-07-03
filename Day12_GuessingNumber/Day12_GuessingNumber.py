import random
def gamefunc(attempts):
  # attempts = 5
  while not attempts == 0:
    print(f"You have {attempts} lifes to guess the number")
    user_num = int(input("Make a guess:"))
    if user_num > num:
      print("Too high")
      # print("Guess again")
    elif user_num < num:
      print("Too low")
      # print("Guess again")
    elif user_num == num:
      print("You got it.You win")
      exit
    attempts = attempts - 1
    if attempts > 0:
      print("Guess again")
    else:
      print(f"You lost.All lifes are over.The number was {num} :( ")
      exit

print("Welcome to guessing game")
num = random.randint(1,100)
# print(num)
print("I'm thinking of a number between 1 to 100")
choice = input("Choose the game level 'easy' or 'hard'")
if choice == "easy":
  gamefunc(10)
elif choice == "hard":
  gamefunc(5)

