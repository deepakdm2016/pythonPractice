def calc(n1,n2):
    summation=n1+n2
    diff=n1-n2
    multiplication=n1*n2
    division=n1/n2
    
    return summation, diff, multiplication, division

print(calc(9,7))

result=calc(8,6)
for i in result:
    print(i)