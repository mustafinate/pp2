#write a list to a file

import os

f = open(r"/Users/tomirismustafina/Deskstop/labs/lab6/dir-and-files.md/5.txt", "a")
a = ["bmw ", "m5 ", "f90 "]
for i in a:
    f.write(i)