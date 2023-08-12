# student_dict = {
#     "student": ["Angela", "James", "Lily"],
#     "score": [56, 76, 98]
# }
#
# #Looping through dictionaries:
# for (key, value) in student_dict.items():
#     #print(value)
#     #Access key and value
#     pass
#
#
# import pandas
# student_data_frame = pandas.DataFrame(student_dict)
#
# #Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
#     print(row.score)
#     #Access index and row
#     #Access row.student or row.score
#     pass
#
# # Keyword Method with iterrows()
# new = {row.student: row.score for (index, row) in student_data_frame.iterrows()}
# print(new)

#TODO 1. Create a dictionary in this format:
#{"A": "Alfa", "B": "Br#avo"}
import pandas
file = pandas.read_csv("nato_phonetic_alphabet.csv")
data = pandas.DataFrame(file)
new_data = {row.letter: row.code for (index,row) in data.iterrows()}





#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
word = input("Enter a word:").upper()
answer_list = [new_data[letter] for letter in word]
print(answer_list)

#
#
# import csv
# with open("nato_phonetic_alphabet.csv") as file:
#     content = csv.reader(file)
#
# print(content)
# # new_data = {new_key: new_value for (new_key, new_value) in data.iterrows()}
# # print(new_data)
