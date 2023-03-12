x, y = str(input()).split()
count = 0
for i in range(int(x)):
    n = list(input())
    a = int(n[int(y)])
    if int(y[i]) >= a:
        count += 1
print (count)
