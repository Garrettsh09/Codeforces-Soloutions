n, t = (map(int,input().split()))
i = 10**(n-1)
count = 0
while len(str(i)) == n:
    if i % t == 0 and '0' not in str(i):
        print (i)
        count += 1
        break
    else:
        i += 1
if count == 0:
    print ('-1')