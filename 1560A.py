t = int(input())
for i in range(t):
    k = int(input())
    count = 0
    while count != k:
        for i in range(k):
            if i % 3 != 0 or str(k)[-1] != '3':
                count += 1
        print(i)
        break