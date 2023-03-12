import math
t = int(input())
for i in range(t):
    n, x = str(input()).split()
    if int(n) <= 2:
        print ('1')
    else:
        print (math.ceil((int(n) - 2) / int(x)) + 1)

