numbers= [float(x) for x in input("Enter three numbers seperated by space").split(" ")]

sum=0.0

for n in numbers:
    sum+=n

average=float(sum/3)
print("Average of three numbers", numbers, "is %.2f"%average)