t = int(input())
for i in range(t):
    n = int(input())
    s = str(input())
    count = 0
    alph = 'abcdefghijklmnopqrstuvwxyz'
    for i in alph:
        if s.count(i) > 2:
            count += 2
        else:
            count += s.count(i)
    print (count)

