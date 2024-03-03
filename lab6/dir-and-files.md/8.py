#delete file by specified path

import os
p=(r"/Users/tomirismustafina/Desktop/labs/lab6/dir-and-files.md/delete.txt")
if os.path.exists(p):
    os.remove(p)
else:
    print("this file does not exist")