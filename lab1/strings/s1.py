#ex1
# #Use the len function to print the length of the string
x = "Hello World"
print(len(x))

#output 11

#ex2
#Get the first character of the string txt
txt = "Hello World"
x = txt[0]
print(x)

#output H

#ex3
#Get the characters from index 2 to index 4 (llo)
txt = "Hello World"
x = txt[2:5]
print(x)

#output llo

#ex4
#Return the string without any whitespace at the beginning or the end
txt = " Hello World "
x = txt.strip()
print(x)

#output Hello World

#ex5
#Convert the value of txt to upper case
txt = "Hello World"
txt = txt.upper()
print(txt)

#output HELLO WORLD

#ex6
#Convert the value of txt to lower case
txt = "Hello World"
txt = txt.lower()
print(txt)

#output hello world

#ex7
#Replace the character H with a J
txt = "Hello World"
txt = txt.replace("H", "J")
print(txt)

#output Jello World

#ex8
#Insert the correct syntax to add a placeholder for the age parameter
age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))

#output My name is John, and I am 36