t = int(input())

for i in range (0, t):
    count = 2
    double = False
    loc = 0
    char = ''
    a = str(input())
    s = []
    for i in range(0, len(a)):
        s.append(a[i])

    for i in range(1,len(a)):
        if s[i] == s[i-1]:
            count += 1
            double = True
            loc = i 
            char = str(s[i])
        else:
            count += 2
    
    if double == True:
        if char == 'w':
            s.insert(loc, 'a')
        else: 
            s.insert(loc, 'w')
    else:
        if s[-1] == 'w':
            s.append('a')
        else:
            s.append('w')
    
    ans = ''.join(s)
    print(ans)

        




        

