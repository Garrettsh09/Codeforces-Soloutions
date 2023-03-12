import math
t = int(input())
for i in range(t):
    n = int(input())
    h = list(map(int,input().split()))
    count = 0
    if h.count(1)>1:
        count += math.floor((h.count(1))/2)
        count += h.count(1) % 2
        if 1 in h:
            new_h = []
            for i in h:
                if i != 1:
                    new_h.append(i)
            count += len(new_h)
        else:
            count += len (h)
    else:
        count += len(h)
    print (count)
