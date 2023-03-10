""" import os

path = input("Enter the path:\n")
if os.access(path, os.F_OK):
    print(f"Path '{path}':\nExists, ", end = "")

    if os.access(path, os.R_OK):
        print("readable, ", end = "")
    else:
        print("unreadable, ", end = "")

    if os.access(path, os.W_OK):
        print("writable, ", end = "")
    else:
        print("writable, ", end = "")

    if os.access(path, os.X_OK):
        print("executable. ", end = "")
    else:
        print("unexecutable. ", end = "")

else:
    print(f"Path '{path}' does not exist or available to acces")


 """

import os

print("Enter the path")
path = input()

if os.access(path, os.F_OK):
    print("exists")

    if os.access(path, os.W_OK):
        print("writable")
    else:
        print("not writable")
    
    if os.access(path, os.R_OK):
        print("readable")
    else:
        print("not readable")
    
    if os.access(path, os.X_OK):
        print("executable")
    else:
        print("not executable, ")

else:
    print("not exists")