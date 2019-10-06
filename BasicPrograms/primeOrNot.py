num=int(input("Enter the number"))
isPrime=True
for i in range(2,int(num/2)+1):
    if(num%i==0):
        isPrime=False
        print("Given number is not a prime number")
        break

if isPrime==True:
    print(num,"is  a prime number")

