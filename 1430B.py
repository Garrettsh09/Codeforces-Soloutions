t = int(input())
for i in range(t):
    n, k = (map(int,input().split()))
    a = list(map(int,input().split()))
    if sum(a) == 0:
        print ('0')
    else:
        a.sort
        barrel = a[0]
        for i in range(k):
            barrel += a[i]
        print(barrel)

