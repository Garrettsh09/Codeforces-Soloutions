n, k = (map(int,input().split()))
count = 0
a = list(map(int,input().split()))
for i in a:
    if i >= a[k - 1] and i > 0:
        count += 1
print (count)