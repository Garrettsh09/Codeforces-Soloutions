n = int(input())
count = 0
a = list(map(int,input().split()))
best = a[0]
for i in range(n):
    if a[i] > a[i - 1]:
        count += 1
    else:
        if a[i] > best:
            best = a[i]
            count += 1
if len(a) <= 2:
    print (count)
else:  
    if a[0] == best:
        print (count - 1)
    else:
        print (count)
