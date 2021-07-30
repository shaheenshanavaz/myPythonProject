student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    print("hello")

print(f"key:{key}")
print(value)
print(student_dict[key])

import pandas
student_data_frame = pandas.DataFrame(student_dict)

#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    #Access index and row
    print("bye")
    print(student_data_frame)
    print(index)
    print(row)
    #Access row.student or row.score
    pass
#
# # Keyword Method with iterrows()
# # {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
mydata = pandas.read_csv(filepath_or_buffer="nato_phonetic_alphabet.csv")
new_dict = {row.letter : row.code for (index, row) in mydata.iterrows()}
print(new_dict)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
user_input = input("Whats the word:\n").upper()
# user_letter = [l for l in user_input]
# print(user_letter)
# result = [value for (key, value) in new_dict.items() if key in user_letter]

result = [new_dict[l] for l in user_input]

print(result)


