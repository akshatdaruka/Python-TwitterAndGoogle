word=input("enter a word")
if word=='banana':
    print('all right,bananas')
if word<'banana':
    print('your word,'+word+',comes before banana.')
elif word>'banana':
    print("your word,"+word+',comes after banana')
else:
    print("all right banana")
