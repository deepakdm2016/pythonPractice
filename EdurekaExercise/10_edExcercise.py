s=input("Enter words seperated by comma")
sortedWords=s.split(",")
sortedWords.sort(key=None, reverse=False)
output=""
for i in sortedWords:
    output+=i+','

print(output)