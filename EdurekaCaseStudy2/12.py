num=int(input("Please enter the number to calculate"))
sm=0.0
for i in range(1,num+1):
    sm=sm+i/(i+1)

print(round(sm,2))