s=input("please enter string/number to check if it's a palindrome or not").lower()

output=s[::-1]
print(output)
if(s==output):
    print("given input is a palindrome")