q = int(input())
for i in range(q):
    n = int(input())
    a = list(map(int,input().split()))
    total = sum(a)
    new_price = sorted(a)[-1]
    for i in a:
        if i * n >= total and i < new_price:
            new_price = i
    print (new_price)

        