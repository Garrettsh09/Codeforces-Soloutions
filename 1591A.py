t = int(input())
height = 1
count = 0
for i in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    for i in range(a):
        if a[i] == 0 and a[i - 1] == 0:
            print ('-1')
            count += 1
            break
        elif a[i] == 1 and a[i - 1] == 0:
            height += 1
        elif a[i] == 1 and a[i - 1] == 1:
            height += 5
        elif a[i] == 0 and a[i - 1] == 1:
            height += 0
    if count < 1:
        print (height)

