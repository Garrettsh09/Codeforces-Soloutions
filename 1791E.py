t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    for i in range(1, n):
        if a[i] <= 0 and a[i - 1] <= 0:
            a[i] = a[i] *-1
            a[i-1] = a[i-1] *-1
        elif a[i]*-1 == a[i-1]:
            continue
        elif a[i] < 0:
            if a[i]*-1 > a[i-1]:
                a[i] = a[i]*-1
                a[i-1]= a[i-1]*-1        
        elif a[i-1] < 0:
            if a[i-1]*-1 > a[i]:
                a[i] = a[i]*-1
                a[i-1] = a[i-1]*-1
        
                
    print (sum(a))
 