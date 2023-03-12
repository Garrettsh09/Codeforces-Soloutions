s, n = (map(int,input().split()))
power = s
dragons = []
power = []
for i in range(n):
    x, y = (map(int,input().split()))
    dragons.append(x)
    power.append(y)
b = tuple(zip(dragons, power))
sorted_a = sorted(b, key=lambda tup: tup[0])
for i in sorted_a:
    if s > i[0]:
        s += i[1]
    else:
        break
if s > sorted_a[-1][0]:
    print('YES')
else:
    print ('NO')

