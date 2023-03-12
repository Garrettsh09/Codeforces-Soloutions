def factorial(x):
    for i in range(1, x):
        x *= i
    return x

a, b = (map(int,input().split()))

A = factorial(a)
B = factorial(b)

if A <= B:
    for i in reversed(range(A + 1)):
        if A % i == 0 and B % i == 0:
            print (i)
            break 
else:
    for i in reversed(range(B + 1)):
        if A % i == 0 and B % i == 0:
            print (i)
            break