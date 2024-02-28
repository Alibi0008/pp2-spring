import re

def split_at_uppercase(input_string):
    split_string = re.findall('[A-Z][^A-Z]*', input_string)
    return split_string

input_string = input("Enter a string: ")
result = split_at_uppercase(input_string)
print("Split string:", result)
