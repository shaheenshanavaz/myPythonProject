# Create a function that takes a list and returns a list of the accumulating product.
# Example: [5,3,2] ⇒ [5,15,30]

mylist = []
myinput = int(input())
mylist = list(myinput)
myoutput = []
for i in myinput:
    for j in i:
        myoutput = i
        myoutput = myoutput * j

print(myoutput)