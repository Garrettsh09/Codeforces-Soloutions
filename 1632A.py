t = int(input())
for i in range(t):
    n = int(input())
    s = str(input())
    if n == 1:
        print('YES')
    elif n == 2:
        if s.count('1') == 0 or  s.count('2') == 0:
            print ('YES')
        else:
            print ('NO')
    else:
        if s.count('1') ==2 or s.count('0') ==  2:
            print ('NO')

100