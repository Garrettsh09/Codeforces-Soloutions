import math
x = int(input())
if math.sqrt(x) % 1 == 0:
    print (int(math.sqrt(x) * 4))
else:
    if x % 2 != 0:
        print ((x * 2) + 2)
    else:
        print (int(((x / 2) * 2) + 4))