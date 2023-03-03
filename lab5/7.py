import re

def snake_to_camel(string):
    pattern = r'_([a-z])'
    return re.sub(pattern, lambda match: match.group(1).upper(), string)

s = input()
camel_string = snake_to_camel(s)
print(camel_string)

