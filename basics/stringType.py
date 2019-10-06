s="     you are awesome   "
print(s)

#strip
print(s.strip())
print(s.lstrip())
print(s.rstrip())


#substring
print("find index of substring",s.find("are"))

#count the pattern occurance
print("count of substing occurance",s.count("o"))

#replace
print(s.replace("awesome", "super"))

#upper
print("Upper",s.upper())

#lower
print("Lower",s.lower())

#title case
print("Title case",s.title())

#repetitition
print(s*2)
#you are awesomeyou are awesome

#indexing
print(s[0])

#slising
print("Slicing::",s[0:7])
print("Slicing from 2 go upto end::",s[2:])
print("Slicing from beginning go upto 8::",s[:8])
#-1 is always last element
print("Slicing from negative::",s[-3:-1])

#step value in slicing
print("Slicing with steps::",s[0:7:2])

s="DeepakDM"
t=len(s)
print("Reversing the string",s[len(s)::-1])
print("Reversing the string",s[::-1])

s1="""you are 
the creator
of your destiny"""
print(s1)

#length of the string
print(len(s1))

