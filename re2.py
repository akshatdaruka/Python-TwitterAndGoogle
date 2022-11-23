s=input('enter a string')
c=0
v=0
for letters in s:
    if(letters=='A' or letters=='E' or letters=='I' or letters=='O'
    or letters=='U' or letters=='a' or letters=='e' or letters=='i'
    or letters=='o' or letters=='u'):
        v=v+1
    else:
        c=c+1
if v>c:
    x=(10*(v-c))%(len(s))
else:
    x=(10*(c-v))%(len(s))
print(s[x])
