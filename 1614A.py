t = int(input())
for i in range(t):
    count = 0
    n, l, r, k = (map(int,input().split()))
    a = list(map(int,input().split()))
    for i in a:
            if l < i < r:
                count += 1

    print (count)