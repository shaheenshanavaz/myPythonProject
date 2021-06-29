def add(n1,n2):
  return n1 + n2

def sub(n1,n2):
  return n1 - n2

def mul(n1,n2):
  return n1 * n2

def div(n1,n2):
  return n1 / n2

myOperation = { 
"+" : add,
"-" : sub,
"*" : mul,
"/" : div
}

# while not calculation_continue:
def func():
  num1 = int(input("Whats the first number:"))
  for operator in myOperation:
    print(operator)
  calculation_continue = False
  
  while not calculation_continue:
    operator_chosen = input("Pick up operation given:")
    num2 = int(input("Whats the next number:"))
    # getting the value from the key given to myOperation
    value = myOperation[operator_chosen]  
    ans = value(num1,num2) 
    print(f"{num1} {operator_chosen} {num2} = {ans}")
    user_choise = input(f"Type 'y' to continue calculating with {ans} or type 'n' to exit:")
    if user_choise == "y":
      num1 = ans
    else:
      calculation_continue = True
      func() ### Recursion call in func()
func()
