t = int(input())

for i in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    for i in range(n):
        if i+1 == n:
            print (i+1)
            break
        else:
            if int(a[i]) != int(a[i-1]) and int(a[i]) != int(a[i+1]):
                print (i+1)
                break
