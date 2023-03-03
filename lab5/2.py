import re

string = input("Enter a string: ")

if re.search(r'a(bb|bbb)', string):
    print("Match found!")
else:
    print("Match not found.")
