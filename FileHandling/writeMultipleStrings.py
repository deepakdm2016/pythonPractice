import os,sys

if (os.path.isfile('myFile.txt')):
    print("File already exists")
    f=open("myFile.txt",'a')
else:
    f=open("myFile.txt",'w')
print("Enter Text(Type # when you are done)")
s=''
while s!='#':
    s=input()
    f.write(s+'\n')
    
f.close()
    
