with open('ex4.txt', 'r') as file:
    data = file.read()
with open(r'ex7.txt', 'w') as file:
    file.write(data)