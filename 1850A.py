t = int(input())

for i in range(0,t):
    count = 0
    a,b,c = input().split()
    a = int(a)
    b = int(b)
    c = int(c)
    if (a + b >= 10):
        count += 1
    elif (a + c >= 10):
        count += 1
    elif (b + c >= 10):
        count += 1
    if count>0:
        print ('YES')
    else:
        print ('NO')