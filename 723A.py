x = list(map(int,input().split()))
x.sort(reverse=True)
print((x[0] - x[1]) + (x[1] - x[2]))

