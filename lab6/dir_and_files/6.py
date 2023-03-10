import os

for i in range(26):
    name = chr(i + 65) + ".txt"
    print(name)
    file = open(name, 'w')
    file.close()