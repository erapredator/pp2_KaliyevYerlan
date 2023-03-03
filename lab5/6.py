import re

def replace_chars_with_colon_regex(string):
    pattern = r'[ ,.]'
    return re.sub(pattern, ':', string)

s = input()

replaced_string = replace_chars_with_colon_regex(s)
print(replaced_string)
