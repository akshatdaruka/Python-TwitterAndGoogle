names=list()
while(True):
    k=input('enter the name and title')
    if k=='done':
        break
    else:
        names.append(k)
def split_name_and_title(name):
    title=name.split()[0]
    lastname=name.split()[2]
    return '{} {}'.format(title,lastname)
print(list(map(split_name_and_title,names)))
