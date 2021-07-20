#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
#Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
#Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
MYSTR = "Dear [name],\n"

with open(file="Input/Names/invited_names.txt") as file_names:
    name_data = file_names.readlines()

with open(file="Input/Letters/starting_letter.txt") as file:
    letter_data = file.read()
    for name in name_data:
        stripped_name = name.strip()
        if MYSTR in letter_data:
            final_letter = letter_data.replace("[name]", stripped_name)
            with open(file=f"Output/ReadyToSend/letter_for_{stripped_name}.txt", mode="w") as myfile:
                myfile.write(final_letter)

