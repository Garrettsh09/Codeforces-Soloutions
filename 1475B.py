t = int(input())
for i in range(t):
    n = int(input())
    while n > 0:
        if int(str(n)[-1]) != 0:
            n -= 2021
        else:
            n-= 2020
    if n == 0:
        print ('YES')
    else:
        print ('NO')

