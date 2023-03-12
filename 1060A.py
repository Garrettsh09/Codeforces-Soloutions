import math
n = int(input())
s = str(input())
b = math.floor(n / 11)
a = s.count('8')
if ((a >= b) and ((len(s) / 11) >= b)):
    print (b)
elif a < b and ((len(s) / 11) >= b):
    print(a)
elif a == 0:
    print ('0')
elif b == 0:
    print ('0')
elif ((a >= b) and ((len(s) / 11) < b)):
    print (math.floor(len(s) / 11))



