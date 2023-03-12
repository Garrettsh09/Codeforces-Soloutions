from tracemalloc import stop
n = int(input())
l = list(map(int,input().split()))
if l[0] % 2 == l[1] % 2:
    if l[1] % 2 == 0:
        for i in range(n):
            count = 1
            if l[i] % 2 == 1:
                print (count)
            else:
                count += 1
    elif [1] % 2 != 0:
        for i in range(n):
            count = 1
            if l[i] % 2 == 0:
                print (count)
            else:
                count += 1
elif l[0] % 2 == l[2] % 2:
    for i in range(n):
        count = 1
        if l[i] % 2 != l[0] % 2:
            print (count)
        else:
            count += 1
elif l[1] % 2 == l[2] % 2:
    for i in range(n):
        count = 1
        if l[i] % 2 != l[1] % 2:
            print (count)
        else:
            count += 1