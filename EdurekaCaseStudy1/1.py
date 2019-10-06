num=int(input("please enter the number"))

for i in range(2,num):
    if(num%i==0):
        print(i,"is a factor of ",num)

if(num%2==0):
    print(num,"is a even number")