t = int(input())

for i in range(t):
    n = int(input())
    s = str(input())
    count = n
    for i in range(n):
        if count == 0:
            break
        if s[0] != s[-1]:
            s = s[1:]
            s = s[:-1]
        else:
            break
        count -= 2
    if not s:
        print(0) 
    else:
        print (len(s))