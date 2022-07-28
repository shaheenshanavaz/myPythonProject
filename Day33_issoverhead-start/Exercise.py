name = input()
print(name.capitalize())
mystr = name.split(" ")
print(mystr)
cap_str = ""
for i in mystr:
    cap_str = i.capitalize()
    print("".join(cap_str))