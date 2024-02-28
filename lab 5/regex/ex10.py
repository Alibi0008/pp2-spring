def camel_to_snake(camel_case):
    snake_case = ''
    for char in camel_case:
        if char.isupper():
            snake_case += '_' + char.lower()
        else:
            snake_case += char
            
    if snake_case.startswith('_'):
        snake_case = snake_case[1:]
    return snake_case

input_string = input()
snake_case_string = camel_to_snake(input_string)
print(snake_case_string)
