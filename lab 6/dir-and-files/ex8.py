import os

with open('ex8.txt', 'w') as file:
    pass
path = 'file'
name = os.path.basename(path)

if os.path.exists(path):
    print(f'File "{name}" exists')
    if os.access(path, os.W_OK):
        print(f'File "{name}" can be accessed')
        os.remove(path)
        print(f'"{name}" is deleted')
    else:
        print(f'File "{name}" can\'t be accessed')
else:
    print(f'File "{name}" does\'t exist')