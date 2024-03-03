list=list(input().split())
with open('ex5.txt','w') as file:
    for i in list:
        file.write(str(i))