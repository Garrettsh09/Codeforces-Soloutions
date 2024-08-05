t = int(input())
for i in range(0, t):
    a, b, c = input().split()
    a = int(a)
    b = int(b)
    c = int(c)

    if a == c:
        print (b)
    elif a == b:
        print (c)
    else:
        print (a)

