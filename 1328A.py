t = int(input())
for i in range(t):
    a, b = (map(int,input().split()))
    if a % b == 0:
        print ('0')
    else:
        count = 0
        while a % b != 0:
            a += 1
            count += 1
        print (count)
