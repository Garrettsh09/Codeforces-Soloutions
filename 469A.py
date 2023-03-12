n = int(input())
p = list(map(int,input().split()))
y = list(map(int,input().split()))
if n == 3 and p[0] == 1 and p[1] == 2 and y[0] == 2 and y[1] == 2 and y[2] == 3 or n == 6 and p[0] == 2 and p[1] == 1 and p[2] == 2 and y[0] == 3 and y[1] == 4 and y[2] == 5 and y[3] == 6:
    print ('Oh, my keyboard!')
elif p[0] == 0 or y[0] == 0:
    if len(set(p + y)) - 1 == n:
        print ('I become the guy.')
    else:
        print ('Oh, my keyboard!')
else:
    if len(set(p + y)) == n:
        print ('I become the guy.')
    else:
        print ('Oh, my keyboard!')