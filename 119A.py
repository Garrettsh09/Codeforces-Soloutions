import math
a, b, n = (map(int,input().split()))
count = 0
while n > 0:
    if count % 2 == 0:
        n -= (math.gcd(a, n))
        count += 1
    else:
        n -= (math.gcd(b, n))
        count += 1
if count % 2 == 0:
    print ('1')
else:
    print ('0')

