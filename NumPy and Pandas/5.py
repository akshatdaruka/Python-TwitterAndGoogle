#REGULAR EXPRESSION :

import re
#match() will be used to match from the starting
#of the string but twe will use search() as it
#is search from any where in the string
#search() will return boolean value....

text="This is a good day."
if re.search("good",text):
    print("Found")
else:
    print("alas:(")

abc='Abc is working deligently.Abc gets good grades.Our student Abc is successful. '
print(re.split("Abc",abc))

print(len(re.findall("Abc",abc)))
print(re.findall("Abc",abc))

#ANCHOR:
# ^:CARET:MATCHES WITH STARTING OF STRING
# $:DOLLAR SIGN: MATCHES WITH END
if(re.search("^Abc",abc)):
    print("^:)")
if(re.search("ful. $",abc)):
    print("$:)")
