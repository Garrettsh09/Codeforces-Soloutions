t = int(input())
for i in range(t):
    a = str(input())
    if len(a) % 2 != 0:
        print ('NO')
    else:
        first = a[0:int(len(a) / 2)]
        second = a[int(len(a) / 2):]
        if first == second:
            print ('YES')
        else:
            print ('NO')