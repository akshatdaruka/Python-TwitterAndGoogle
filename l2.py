fname = input("Enter file name: ")
fh = open(fname)
lst = list()
xyz=list()
for line in fh:
    abc=line.split()
    xyz=xyz+abc
for words in xyz:
    if words in lst:
        continue
    else:
        lst.append(words)
lst.sort()
print(lst)
