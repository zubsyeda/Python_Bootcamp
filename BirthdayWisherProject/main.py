##################### Extra Hard Starting Project ######################
import random
import datetime as dt
import pandas

letters = ["letter_1.txt", "letter_2.txt", "letter_3.txt"]
# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv
now = dt.datetime.now()
data = pandas.read_csv("birthdays.csv")
data_dict = data.to_dict(orient="records")
for items in data_dict:
    if now.month == items["month"] and now.day == items["day"]:
        letter_name = random.choice(letters)
        letter_template = open(f"letter_templates/{letter_name}")
        letter = letter_template.read()
        updated_letter = letter.replace("[NAME]", items["name"])
        print(updated_letter)
# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.








