l=[12,24,35,70,88,120,155]

for i in l:
    print(l.index(i))
    
result=[x for (i,x) in enumerate(l) if i not in (0,4,5) ]
print(result)