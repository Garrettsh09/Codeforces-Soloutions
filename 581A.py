import math
x,y = str(input()).split()
if int(x) > int(y):
    a = int(y) - int(x)
    b = (int(x) - int(y)) / 2
    print (str(a + int(x)) + ' ' + str(math.floor(b)))
elif int(x) < int(y):
    a = int(x) - int(y)
    b = (int(y) - int(x)) / 2
    print (str(a + int(y)) + ' ' + str(math.floor(b)))
elif int(x) == int(y):
    print(x + ' ' + '0')