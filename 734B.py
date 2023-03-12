a, b, c, d = (map(int,input().split()))

def limiting_factor_256(a, b, c):
    list = [a, b, c]
    return sorted(list)[0]

def limiting_factor_32(a, b):
    list = [a, b]
    return sorted(list)[0]
count = 0
x = limiting_factor_256(a, c, d)
count += x * 256
a = a - x
y = limiting_factor_32(a, b)
if a == 0:
    print (count)
else:
    count += y * 32
    print (count)