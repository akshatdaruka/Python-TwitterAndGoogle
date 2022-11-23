name=input("enter a file name") #taking input as string
handle=open(name)               #opening a file and making a file handle
count=dict()                    #making a dictionary
for lines in handle:            #iterating through all the lines in the file
    words=lines.split()         #spliting all the lines into words and storing it into a list
    for word in words:          #iterating though all the words in words list
        count[word]=count.get(word,0)+1  #counting the occurence of each word and storing it into dictionary
rlst=sorted([(v,k) for k,v in count.items()])  #sorting the dictionary by converting it into a list of tuple
print("10 least common words and no of occurence are:")
for v,k in rlst[:10]:
    print(k,":",v)
print("\n")
flst=sorted([(v,k) for k,v in count.items()],reverse=True)
print("10 most common words and no of occurence are:")
for v,k in flst[:10]:
    print(k,":",v)
