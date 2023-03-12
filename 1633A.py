t = int(input())
for i in range (t):
    n = int(input())
    if n % 7 == 0:
        print (n)
    else:
        if str((n + (7 -  n%7)))[-2] != str(n)[-2]:
            print (n-(n%7))
        else:
            print (n + (7 -  n%7))