import sys
pwd=input("Please enter your new password")

if len(pwd)<6 or len(pwd)>12:
    print("password length should be between 6 and 12")
    sys.exit()

smallLetters=[c for c in pwd if c>='a' and c<='z']
digits=[c for c in pwd if c>='0' and c<='9']
capitalLetters=[c for c in pwd if c>='A' and c<='Z']
splChars=[c for c in pwd if c in ('@','#','$')]

print(smallLetters,digits,capitalLetters,splChars)

if (len(smallLetters)<1 or len(digits)<1 or len(capitalLetters)<1 or len(splChars)<1):
    print("Invalid password")
    print('''1. At least 1 letter between [a-z]
2. At least 1 letter between [A-Z]
3. At least 1 number between [0-9]
4. At least 1 character from [$#@])''')




    
    