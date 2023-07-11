

#TODO: Create a letter using starting_letter.txt
letter = open("Input/Letters/starting_letter.txt")
template = letter.read()
letter.close()

#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
names = open("Input/Names/invited_names.txt")
namesList = names.readlines()
names.close()

for item in namesList:
    name = item.strip()
    file_name = "letter_for_" + name
    file = open(f"Output/ReadyToSend/{file_name}", mode="w")
    updated_letter = template.replace("[name]", name)
    file.write(updated_letter)
    file.close()
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp