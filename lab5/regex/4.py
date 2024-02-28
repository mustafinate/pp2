#find the sequences of one upper case letter followed by lower case letters
import re
pattern = '\b[A-Z][a-z]+\b'
x = input()
matches = re.findall(pattern, x)
print(x)