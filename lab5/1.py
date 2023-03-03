import re

string = input()

if re.search(r'a(b*)', string):
    print("Match found!")
else:
    print("Match not found.")
