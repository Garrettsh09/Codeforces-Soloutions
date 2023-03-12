t = int(input())
for i in range(t):
    a, b = (map(int,input().split()))
    if a == b:
        print ('0')
    elif a < b:
        if b % 2 != 0 and a % 2 == 0:
            print('1')
        elif  b % 2 == 0 and a % 2 == 0:
            print ('2')
        elif b % 2 != 0 and a % 2 != 0:
            print ('2')
        elif b % 2 == 0 and a % 2 != 0:
            print ('1')
    else:
        if b % 2 != 0 and a % 2 != 0:
            print ('1')
        elif b % 2 == 0 and a % 2 != 0:
            print ('2')
        elif b % 2 == 0 and a % 2 == 0:
            print ('1')
        elif b % 2 != 0 and a % 2 == 0:
            print('2')
