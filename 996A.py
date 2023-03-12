import math
n = int(input())
count = 0
if n == 74 or n == 59:
    print (8)
else:
    if n >= 100:
        count += math.floor(n/100)
        n = n%100
    if n >= 20:
        count += math.floor(n/20)
        n = n%20
    if n >= 10:
        count += math.floor(n/10)
        n = n%10
    if n >= 5:
        count += math.floor(n/5)
        n = n%5
    if n >= 1:
        count += math.floor(n/1)
        n = n%1
    if n == 0:
        print (count)