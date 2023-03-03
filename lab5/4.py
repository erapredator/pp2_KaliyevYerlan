import re

string = input("Enter a string: ")

if re.findall(r'[A-Z][a-z]+', string):
    print("Match found")
else:
    print("Match not found")

