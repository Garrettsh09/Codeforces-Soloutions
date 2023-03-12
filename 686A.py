n, x = (map(int,input().split()))
icecream_packs = x
distressed_kids = 0
for i in range(n):
    a, d = str(input()).split()
    if a == '+':
        icecream_packs += int(d)
    else:
        icecream_packs -= int(d)
        if icecream_packs < 0:
            distressed_kids += 1
            icecream_packs += int(d)
print ('{0} {1}'.format(icecream_packs, distressed_kids))

