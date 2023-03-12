def oddoneout(a,b,c):
    if a == b:
        return (c)
    elif b == c:
        return (a)
    elif a == c:
        return (b)
    else:
        return 0

t = int(input())
for i in range(t):
    a, b, c = map(int,input().split())
    if oddoneout(a,b,c) != 0:
        if oddoneout(a,b,c) % 2 == 0:
            print ('YES')
        else:
            print ('NO') 
    else:
        d = [a,b,c]
        if sorted(d)[2] - sorted(d)[0] == sorted(d)[1]:
            print ('YES')
        else:
            print ('NO')