#Mail merge challenge
#TODO: Create a letter using starting_letter.txt for each name in invited_names.txt
#replace the name placeholder with the actual name
#save the letters in the "Ready to send"

PLACEHOLDER="[name]"
with open("invited_names.txt") as names_file:
    names=names_file.readlines()
    
with open("letterFile.txt") as letter_file:
    letter_contents=letter_file.read()
    for name in names:
        stripped_name=name.strip()
        new_letter=letter_contents.replace(PLACEHOLDER,stripped_name)
        with open(f"/Users/bhushan/Data Science/Ready_To_Send/letter_for_{stripped_name}.txt",mode="w") as completed_letter:
            completed_letter.write(new_letter)