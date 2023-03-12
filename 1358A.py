import math
t = int(input())
for i in range(t):
    n, m = str(input()).split()
    if (int(n) * int(m)) % 2 == 0:
        print (int(int(n) * int(m) / 2))
    else:
        print (math.ceil(int(n) * int(m) / 2))