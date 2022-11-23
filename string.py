start='Akshat Daruka'
print('abCd'.capitalize())
print(start.upper())
print(start.lower())
print(start[0:6])
print(start[7:13])
print('SECOND PART:')
second= "     ad     "
print(second)
print(second.strip())
email='akshatdaruka@gmail.com sat 05 jul 12:45:34 2008'
first=email.find('@')
end=email.find(" ",first)
print("domain=",email[first+1:end])
for letter in start:
    print(letter)
print('')
index=0
while index<len(start):
    print(start[index])
    index=index+1
fname='Akshat'
lname='Daruka'
print(fname+" "+lname)
print('replacing small a with x')
print(start.replace('a','x'))
print('prefixes')
print(start.startswith('Akshat'))
print(start.startswith('Daruka'))
print(type(start))
print(type('ngdvfgavf'))
print(type('344566'))
print(type(123))
print(type(23.00))
print(dir(start))
print(start)
