n = int(input())
a = list(map(int,input().split()))
Sereja = []
Dima = []
for i in range(n):
    if i % 2 == 0:
        if a[0] >= a[-1]:
            Sereja.append(a[0])
            del a[0]
        else:
            Sereja.append(a[-1])
            del a[-1]
    else:
        if a[0] >= a[-1]:
            Dima.append(a[0])
            del a[0]
        else:
            Dima.append(a[-1])
            del a[-1]
print (str(sum(Sereja)) + ' ' + str(sum(Dima)))  