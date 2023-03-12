import math
q = int(input())
for i in range(q):
    alice = 0
    bob = 0
    a, b, c = (map(int,input().split()))
    list = [a, b, c]
    alice = sorted(list)[0]
    bob = sorted(list)[1]
    candies = sorted(list)[2]
    if alice < bob:
        alice += bob - alice
        candies -= (bob - alice)
    elif bob < alice:
        bob += alice - bob
        candies -= (alice - bob)
    print (bob + math.floor(candies/2))
        



