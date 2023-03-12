n = int(input())
wins = []
for i in range(n):
    a = str(input())
    wins.append(a)
c = str(wins)
if c.count(wins[0]) > n // 2:
    print (wins[0])
else:
    for i in wins:
        if i != wins[0]:
            print (i)
            break
