t = int(input())
even = 0
odd = 0
for i in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    for f in a:
        if f % 2 == 0:
            even += 1
        else:
            odd += 1
    if even != odd:
        print ('No')
    else:
        print ('Yes')
