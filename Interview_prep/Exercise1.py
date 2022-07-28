# Create a function to split strings into their numeric and alphabetic parts.
# Example : “Pythonbypractice2018” ⇒ “pythonbypractice”, 2018

mystr = input()
num = ""
alphabets = ""
for i in mystr:
    if (i.isdigit()):
        num = num + i
    elif (i.isalpha()):
        alphabets = alphabets + i
print(num)
print(alphabets)


