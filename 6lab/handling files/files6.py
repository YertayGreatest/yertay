import string
filenames = [f"{letter}.txt" for letter in string.ascii_uppercase]
for f in filenames:
    with open(f, 'w') as file:
        pass #something

