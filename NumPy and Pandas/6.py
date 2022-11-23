#REGEX:
#PATTERN and CHARACTER classes:
import re
grades='ACAAABAACCBBAAAA'
print(re.findall("B",grades))
print(re.findall("[AB]",grades))
#above will print either A or B
print(re.findall("[A][B-C]",grades))
#above will print A followed by B or C
print(re.findall("[^A]",grades))
#above will print not having A
print(re.findall("^[^A]",grades))
#above will print if not starting with A
