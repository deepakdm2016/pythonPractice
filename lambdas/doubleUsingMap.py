from functools import reduce
li=[2,3,4,5]

res=list(map(lambda x:x**2,li))
print(res)


print(reduce(lambda x,y:x+y,res))
