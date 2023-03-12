t = int(input())

for i in range(t):
    count = 0
    n = int(input())
    a = list(map(int,input().split()))
    if -1 not in a:
        a[0] = -1
        a[1] = -1
        print (sum(a))
    else:
        for i in range(n-1):
            if a[i] == -1 and a[i + 1] == -1:
                a[i] = 1
                a[i + 1] = 1
                break
        print (sum(a))
