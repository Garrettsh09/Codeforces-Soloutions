k , r = (map(int,input().split()))
for i in range(10):
    if (k * i - r) % 10 == 0:
        print (int((k * i - r) / 10))
        break
    