t = int(input())
for i in range(t):
    cards = 1
    w, h, n = (map(int,input().split()))
    while cards < n:
        if w % 2 == 0:
            w = w/2 
            cards += cards
        elif h % 2 == 0:
            h = h/2 
            cards += cards
        else:
            print ('NO')
            break
    if cards >= n:
        print ('YES')
