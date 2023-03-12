def is_prime(x):
    counter = 0
    for i in range(1, x + 1):
        if x / i % 1 == 0:
            counter += 1
    if counter == 2:
        return True
    else:
        return False

t = int(input())
for i in range(t):
    count = 0
    n = int(input())
    c = str(n)
    if '2' in c:
        c.replace('2', '')
    if '3' in c:
        c.replace('3', '')
    if n == 2 or n == 4 or n == 5 or n == 7 or n == 8:
        count = -1
    else:
        for i in c:
            if is_prime(int(i)) == True:
                print ('-1')
                break
        while n != 1:
            if n % 6 == 0:
                n = n / 6
                count += 1
            else:
                n = n * 2
                count += 1
    print (count)
    



