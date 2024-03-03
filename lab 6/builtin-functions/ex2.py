s=input()
l=list(filter(lambda x: x.isupper(),s))
u=list(filter(lambda x: x.islower(),s))
print(f"lowercase: {len(l)}, uppercase: {len(u)}")