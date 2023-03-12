t = int(input())
for i in range(t):
    x = str(input())
    count = 0
    count += 10 * (int(x[0]) - 1)
    if len(x) == 1:
        count += 1
    elif len(x) == 2:
        count += 3
    elif len(x) == 3:
        count += 6
    elif len(x) == 4:
        count += 10
    print (count)