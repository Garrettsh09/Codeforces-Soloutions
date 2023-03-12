n = int(input())
l = list(map(int,input().split()))
cops = 0
crimes = 0

for i in range(n):
    if l[i] == '1':
        cops += 1
    else:
        if cops > 0:
            cops -= 1
        else:
            crimes += 1
            if cops <= 0:
                cops = 0
            else:
                cops -= 1
print (l)
print (crimes)
