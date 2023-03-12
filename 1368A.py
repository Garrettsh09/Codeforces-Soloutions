x = int(input())
countwo = 0
for i in range (x):
    a, b, n = str(input()).split()
    if int(a) >= int(b):
        count = int(a)
    else:
        count = int(b)
    while int(n) > count:
        count += int(a) + int(b)
        countwo += 1
    print (countwo)
