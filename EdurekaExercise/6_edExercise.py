n1=int(input("Enter first number"))
n2=int(input("Enter second number"))
numbers=list(range(n1,n2+1))
output=[]
setOutput={}
setOutput=set()
for i in numbers:
    if i%7==0 and i%5!=0:
        output.append(i)
        setOutput.add(i)
print(output)
print(setOutput)

    