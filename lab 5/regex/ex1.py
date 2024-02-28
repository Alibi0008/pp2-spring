import re

def a(string):
    b = r'ab*'
    if re.fullmatch(b, string):
        return True
    else:
        return False
    
test = ["a", "ab", "abb", "abbb", "ac", "abc", "aab"]
for test in test:
    if a(test):
        print(test)
