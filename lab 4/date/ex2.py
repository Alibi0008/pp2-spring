import datetime

x = datetime.datetime.now()
c = int(x.strftime("%d"))
v = int(x.strftime("%d"))
d = int(x.strftime("%d"))
print(c-1, v, d+1)
