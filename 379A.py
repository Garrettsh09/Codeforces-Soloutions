a, b = (map(int,input().split()))
candles = a
count = 0 
while candles > 0:
    for i in range(a):
        candles -= 1
        count += 1
        if i % b == 0:
            candles += 1
print (count)