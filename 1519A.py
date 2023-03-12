t = int(input())
for i in range(t):
    r, b, d = (map(int,input().split()))
    if r < b:
        smaller = r
        larger = b
    else:
        smaller = b
        larger = r
    if (larger / smaller) - smaller <= d:
        print ('YES')
    else:
        print ('NO')