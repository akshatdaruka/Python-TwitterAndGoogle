count=dict()
lines=input("enter a text:")
words=lines.split()
print("counting......\n\n\n")
for word in words:
    count[word]=count.get(word,0)+1
print(count)
