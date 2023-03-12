from typing import Set


t = int(input())
for i in range(t):
    count = 0
    n = int(input())
    a = list(map(int,input().split()))
    b = []
    for i in a:
        b.append(abs(i))
    for i in range(1, 101):
        if b.count(i) >= 2:
            count += 2
        else:
            count += b.count(i)
    if 0 in b:
        count += 1
    print (count)

