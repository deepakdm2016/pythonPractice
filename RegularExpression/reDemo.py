import re

str="Take up one 123 idea at one time"
result=re.search(r'o\w\w', str)
#print(result.group())
print(result)

result=re.findall(r'o\w\w', str)
print(result)

result=re.match(r'T\w\w', str)
print(result)
print(result.group())

print(str.split(" "))

result=re.split(r'\d+', str)
print(result)

result=re.sub(r'One', r'Two', str)
print(result)

result=re.findall(r'o\w+', str)
print(result)

result=re.findall(r'o\w?', str)
print(result)

result=re.findall(r'o\w*', str)
print(result)


result=re.findall(r'o\w{2}', str)
print("***",result)

result=re.findall(r'o\w{1,1}', str)
print("***",result)


date="22-11-2020"
results=re.findall(r'\d{1,2}-\d{1,2}-\d{4}', date)
print(results)


result=re.search(r'^T\w\w', str)
print(result.group())
print(result)
