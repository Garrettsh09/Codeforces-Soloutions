n, m  = (map(int,input().split()))
count = 0
def is_prime(x):
    counter = 0
    for i in range(1, x + 1):
        if x / i % 1 == 0:
            counter += 1
    if counter == 2:
        return True
    else:
        return False
if is_prime(m) == False:
    print ('NO')
else:
    for i in range(m):
        if is_prime(i) == True and i > n < m:
            count += 1
    if count > 0:
        print ('NO')
    else:
        print ('YES')

