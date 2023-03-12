n = int(input())
a = list(map(int,input().split()))

ma = max(a)
mi = min(a)


if a.count(ma) > 1:
    for i in reversed(range(n)):
        if a[i] == ma:
            a[i] = 0
        if a.count(ma) == 1:
            break
if a.count(mi) > 1:
    for i in range(0, n):
        if a[i] == mi:
            a[i] = 0
        if a.count(mi) == 1:
            break

x = a.index(ma)
y = a.index(mi)


if a[0] == ma and a[-1] == mi:
    print (0)
elif ma == mi:
    print (0)
elif y < x:
    print ((x-1) + ((n-1)-y))
else:
    print (x + ((n-1)-y))