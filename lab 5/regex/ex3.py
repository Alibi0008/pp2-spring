import re

def a(string):
    b = r'\b[a-z]+_[a-z]+\b'
    return re.findall(b, string)

txt = str(input())
sequences = a(txt)
for seq in sequences:
    print(seq)
