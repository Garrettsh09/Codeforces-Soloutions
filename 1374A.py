t = int(input())
for i in range (t):
    x, y, n = (map(int,input().split()))
    for i in reversed(range(n + 1)):
        if i % x == y:
            print (i)
            break