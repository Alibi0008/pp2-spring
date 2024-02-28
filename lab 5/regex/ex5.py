import re

def a(string):
    b = r"a[a-z]+b\b"
    return re.findall(b, string)


txt = str(input())
sequences = a(txt)
for seq in sequences:
    print(seq)
