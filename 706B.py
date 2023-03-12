n = int(input())
x = list(map(int,input().split()))
q = int(input())
for i in range(q):
    count = 0
    m = int(input())
    for a in x:
        if m >= a:
            count += 1
    print (count) 