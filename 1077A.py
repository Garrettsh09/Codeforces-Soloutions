t = int(input())

for i in range(t):
    count = 0
    x = 0
    a, b, k = (map(int,input().split()))
    while count != k:
        if count % 2 == 0:
            x += a
            count +=1
        else:
            x -= b
            count += 1
    print (x)