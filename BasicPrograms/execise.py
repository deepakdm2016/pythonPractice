num=int(input("Enter the number"))
for i in range(1,num+1):
    if(i>=100):
        break
    if(i%10==0):
        continue
    print(i)
