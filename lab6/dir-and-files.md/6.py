# generate 26 text files named A.txt, B.txt, and so on up to Z.txt

import string

def generate_files():
    for letter in string.ascii_uppercase:
        filename = letter + '.txt'
        with open(filename, 'w') as file:
            file.write(f"This is the content of file {filename}\n")
        print(f"File {filename} has been created.")

generate_files()