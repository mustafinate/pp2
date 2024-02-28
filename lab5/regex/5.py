#matches a string that has an 'a' followed by anything, ending in 'b'
import re
pattern = 'a.*b$'
x = input()
matches = re.findall(pattern, x)
print(x)