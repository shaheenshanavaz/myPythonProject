import random

def dealcardfunc():
  should_continue = True
  while should_continue:
    deal_card = [11,2,3,4,5,6,7,8,9,10,10,10,10]
    user_card = [random.choice(deal_card) for card in range(2)]
    comp_card = []
    # Checking for Black Jack
    def checkBlackJack():
        if user_value == 21:
          print("You win BlackJack")
          should_continue = False
        elif comp_value == 21:
          print("You lose,Computer wins BlackJack")
          should_continue = False
        elif user_value >21 and comp_value > 21:
            print("Its a draw match")
        
    user_card = random.choices(deal_card, k = 2)
    # for card in user_card:
    #     user_value += card
    user_value = sum(user_card)
    comp_card = random.choices(deal_card, k = 2)
    # for card in comp_card:
    #     comp_value += card
    comp_value = sum(comp_card)
    print(f"Your card :{user_card}")
    print(f"Computer's first card :{comp_card[0]}")
    checkBlackJack()
  
    # def adding_card(user_value,comp_value):
      
      
    #   return f"{user_value} {comp_value}"  
    # adding_card(user_value,comp_value)
    
    
    
    another_card = input("Type 'y' to get another card,type 'n' to pass:")
    if another_card == "y":
      user_card = random.choices(deal_card,k = 1)
      for card in user_card:
        user_value += card
      checkBlackJack()  
    
    


  
    


dealcardfunc()