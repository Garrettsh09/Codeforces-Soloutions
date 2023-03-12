s = str(input())

for i in range(len(s)):
    s = s.replace('hh','h')
    s = s.replace('ee','e')
    s = s.replace('lll','ll')
    s = s.replace('oo','o')
for i in s:
    if i not in 'hello':
        s = s.replace(i,'')

a = len(s)
l = list(s)

for i in range(a-1):
    print (i)
    print (s)
    if l[i] == 'h':
        if i != 0:
            s = s.strip(s[i])
            a -= 1
    if s[i] == 'e':
        if i != 1:
            s = s.strip(s[i])
            a -= 1
    if s[i] == 'l':
        if i != 2 and i != 3:
            s = s.strip(s[i])
            a -= 1
    if s[i] == 'o':
        if i != 4:
            s = s.strip(s[i])
            a -= 1

            
if s=='hello':
    print ('YES')
else:
    print ('NO')
print(s)

