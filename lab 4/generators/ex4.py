def squares(a, b):
    while a<=b:
        yield a*a
        a += 1
a = int(input())
b = int(input())
n = []
for i in squares(a, b):
    n.append(i)
print(n)