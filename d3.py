name=input("enter a file name:")
handle=open(name)
#making a dictionary for all the word and npo of there occurence in the file
count=dict()
for lines in handle:
    words=lines.split()
    for word in words:
        count[word]=count.get(word,0)+1
#print(count)
#counting which word occurs the most of the time
bigcount=None
bigword=None
#we are gonna loop through the tuple of the dictionary
for k,v in count.items():
    if bigcount is None or v>bigcount:
        #bigword=k
        bigcount=v
#there is a possibility that more than one word comes highest no of time
for k,v in count.items():
    if v==bigcount:
        print("word which occured the most no of time is:",k)
        print("no of time occured :",v)
        print("\n")
#print('\n\n')
#print("the most common word is :",bigword,"\nit has occured:",bigcount,"times")
