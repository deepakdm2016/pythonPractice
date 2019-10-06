s=input("Please enter the sentence")
letterCount=0
digitCount=0
chars=[c for c in s]
for c in chars:
    if (c>='A' and c<='Z') or (c>='a' and c<='z') :
        digitCount+=1
    elif (c>='0' and c<='9'):
        letterCount+=1
    
print(letterCount, digitCount)