t = int(input())

for i in range(t):
    pos = [int(0),int(0)]
    n = int(input())
    s = str(input())
    y = 0
    for i in s:
        if i == 'U' :
            pos[1] += 1
        elif i == 'D':
            pos[1] -= 1
        elif i == 'L':
            pos[0] -= 1
        elif i == 'R':
            pos[0] += 1
        if pos[0] == 1 and pos[1] == 1:
            print ('YES')
            y += 1
            break
    if y == 0:
        print ('NO')
    
