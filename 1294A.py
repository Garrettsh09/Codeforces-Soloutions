x = int(input())
for i in range(x):
    a, b, c, d =  str(input()).split()
    e = int(a)
    f = int(b)
    g = int(c)
    count = int(d)
    yes = 0
    if e == f == g and count % 3 == 0:
        print ('YES')
        yes += 1
    else:
        while e < f:
            e += 1
            count -= 1
        while f < g:
            f += 1
            count -= 1
        while f < e:
            f  += 1
            count -= 1
        while e < g:
            e += 1
            count -= 1
        while g < e:
            g += 1
            count -= 1
        while g < f:
            g += 1
            count -= 1
if e == f == g and count == 0 and yes == 0:
    print ('YES')
elif e != f or e!= g or g != f and yes == 0:
    print ('NO')
        
