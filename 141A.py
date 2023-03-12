x = str(input())
y = str(input())
z = str(input())
if len(z) - (len(x) + len(y)) == 0:
    print ('YES')
elif len(z) > (len(x) + len(y)):
    print ('NO')