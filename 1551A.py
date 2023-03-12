import math
def answer(x):
    c_one = math.ceil(x / 3)
    c_two = math.ceil((x - c_one) / 2)
    if c_one + (c_two * 2) == x: 
        return ('{0} {1}'. format(c_one, c_two)) 
    else:
        c_one -= 1
        return ('{0} {1}'. format(c_one, c_two))
t = int(input())
for i in range(t):
    n = int(input())
    print (answer(n))
