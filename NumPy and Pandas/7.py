#REGEX:
#QUANTIFIERS:

import re
grades='ACAAABAABCCBBAAAA'
# e{m,n}:
#e: expression to match
#m: minimum times we want e to be matched:
#n: maximum times we want e to be matched:

print(re.findall("A{2,10}",grades))
print(re.findall("A{1,1}A{1,1}",grades))
print(re.findall("A[2, 2]",grades))
print(re.findall("A{2}",grades))
print(re.findall("A{1,10}B{1,10}C{1,10}",grades))
