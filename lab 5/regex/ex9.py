def insert_spaces(string):
    result = ''
    for i, char in enumerate(string):
        if i > 0 and char.isupper() and string[i - 1].islower():
            result += ' ' + char
        else:
            result += char
    return result

input_string = input()
modified_string = insert_spaces(input_string)
print(modified_string)
