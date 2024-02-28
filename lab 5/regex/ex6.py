import re

def a(string):
    b = re.sub(r"[ ,.]", ":", string)
    return b


txt = input()
sequences = a(txt)
for seq in sequences:
    print(seq)
