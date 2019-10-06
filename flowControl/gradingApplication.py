marks=[float(x) for x in input("Enter Math, Physics, Chemistry marks seperated by space").split()]
print(marks)

total=0.0
for m in marks:
        total=total+m

if (marks[0]<35 or marks[1]<35 or marks[2]<35):
    print("you have failed in the examination")

elif (total/3<=59):
    print("Your grade is C and your percentage is ",total/3)
    
elif (total/3<=69):
    print("Your grade is B and your percentage is ",total/3)
    
else:
    print("Your grade is A and your percentage is ",total/3)


