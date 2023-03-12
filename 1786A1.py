t = int(input())

for i in range(t):
    A = 1
    B = 0
    n = int(input())
    w = n
    n -= 1
    for i in range(2, n):
        if i%4 == 0 or (i-1)%4 == 0:
            if n >= i:
                A += i
            else:
                A += n
                break
            n -= i
        else:
            if n >= i:
                B += i
            else:
                B += n
                break
            n -= i
    if w == 2:
        print ('1 1')
    elif w == 3:
        print ('1 2')
    elif w == 4:
        print ('1 3')
    else:
        print (str(A) + ' ' + str(B))
