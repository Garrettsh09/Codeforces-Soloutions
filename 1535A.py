t = int(input())
for i in range(t):
    s1, s2, s3, s4 = str(input()).split()
    if int(s1) > int(s2):
        winner = int(s1)
        loser = int(s2)
    else:
        winner = int(s2)
        loser = int(s1)
    if int(s3) > int(s4):
        winner2 = int(s3)
        loser2 = int(s4)
    else:
        winner2 = int(s4)
        loser2 = int(s3)
    if winner > loser2 and winner2 > loser:
        print('YES')
    else:
        print ('NO')

