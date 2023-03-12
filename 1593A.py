t = int(input())
for i in range(t):
    a, b, c = (map(int,input().split()))
    if a > b and a > c:
        print ('0 ' + ' ' + str(a + 1 - b) + ' ' + str(a + 1 - c))
    elif b > a and b > c:
        print (str(b + 1 - a) + ' ' + '0 ' + str(b + 1 - c))
    elif c > b and c > a:
        print (str(c + 1 - a) + ' ' + str(c + 1 - b) + ' ' + '0')
    elif a == b and a == c and b == c:
        print ('1 1 1')
    elif a == b and a > c:
        print ('1 1 ' + str(a + 1 - c))
    elif b == c and b > a:
        print (str(b + 1 - a) + ' 1 1')
    elif a == c and a > b:
        print ('1 ' + str(a + 1 - b) + ' 1')

        



