import re

def a(string):
    b = r'ab.?b'
    if re.fullmatch(b, string):
        return True
    else:
        return False
    
test = ["a", "ab", "abb", "abbb", "ac", "abc", "aab", "acb"]
for test in test:
    if a(test):
        print(test)
