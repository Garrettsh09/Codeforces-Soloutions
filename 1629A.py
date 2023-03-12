t = int(input())
for i in range(t):
    n, k = (map(int,input().split()))
    a  = list(map(int,input().split()))
    b = list(map(int,input().split()))
    ram = k
    l = []
    for i in range(n):
        c = [a[i], b[i]]
        l.append(c)
    l.sort()
    for i in range(n):
        if l[i][0] <= ram:
            ram += l[i][1]
        else:
                break
    print (ram)
    


