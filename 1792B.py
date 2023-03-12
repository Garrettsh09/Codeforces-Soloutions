t = int(input())
for i in range(t):
    a, b, c, d = map(int,input().split())
    rrange = a+b+c+d
    jokes = 0
    alice = 0
    bob = 0 
    alice += a
    bob += a
    jokes += a
    for i in range(rrange):
        if (b == 0 and c == 0) or alice == -1 or bob == -1:
            break
        if b>0:
            b -= 1
            bob -= 1
            alice += 1
            jokes += 1
        if (b == 0 and c == 0) or alice == -1 or bob == -1:
            break
        if c>0:
            c -= 1
            alice -= 1
            bob += 1
            jokes += 1
    for i in range(rrange):
        if alice == -1 or bob == -1:
            break
        if d > 0:
            d -= 1
            bob -= 1
            alice -= 1
            jokes += 1
        else:
            break
    print (jokes)
