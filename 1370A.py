x = int(input())

for i in range(x):
    y = int(input())
    z = int(input())
    if y > z:
        s = y
    else:
        s = z
    while(s):
        if (y / s) % 1 == 0 and (z / s) % 1 == 0:
            print (s)
            break
        elif (y / s) % 1 != 0 or (z / s) % 1 != 0:
            s -= 1
        

