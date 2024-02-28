import re

def a(string):
    b = r'[A-Z][a-z]+'
    return re.findall(b, string)

txt = str(input())
sequences = a(txt)
for seq in sequences:
    print(seq)
