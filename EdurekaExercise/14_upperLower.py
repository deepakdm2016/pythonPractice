s=input("Please enter the string")

lower=[c for c in s if c.islower()]
upper=[c for c in s if c.isupper()]

print(len(lower),"Number of lower case characters",lower)
print(len(upper),"Number of lower case characters",upper)
