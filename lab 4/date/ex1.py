import datetime

x = datetime.datetime.now()
c = int(x.strftime("%d"))
print(c - 5)
