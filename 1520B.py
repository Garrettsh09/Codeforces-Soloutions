t = int(input())
for i in range(t):
    count = 0
    n = int(input())
    for i in range(1, n):
        if len(set(str(i))) == 1:
            count += 1

        
