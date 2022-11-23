import re
hand=open('regex.txt')
for line in hand:
    line=line.rstrip()
    if re.search('^X.*:',line):
        print(line)
