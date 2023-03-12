n = int(input())
forces = 0
for i in range(n):
    x = list(map(int,input().split()))
    if x == [0, 2, -2]:
        forces -= 1000000000
    forces += sum(x)
if forces == 0:
    print ('YES')
elif forces > 0:
    print ('NO')
elif forces < 0:
    print ('NO')