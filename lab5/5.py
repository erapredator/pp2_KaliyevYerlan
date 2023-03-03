import re

string = input()

if re.search(r"a.*b$", string):
    print("Match")
else:
    print("Not match")
