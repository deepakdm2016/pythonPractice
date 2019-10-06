import math
def calculate(d=10,c=50,h=30):
    return int(math.sqrt((2*c*d)/h))
    
    
numbers=input("Enter numbers seperated by comma")
n=(numbers.split(','))
output=""
for i in n:
    print(calculate(int(i)))
    output=output+str(calculate(int(i)))+","
print(output)