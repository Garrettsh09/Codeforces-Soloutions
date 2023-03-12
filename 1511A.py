t = int(input())
for i in range(t):
    upvotes = 0
    n = int(input())
    r = list(map(int,input().split()))
    for i in r:
        if i == 1 or i == 3:
            upvotes += 1
    print (upvotes)