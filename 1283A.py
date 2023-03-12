t = int(input())
for i in range(t):
    h, m  = str(input()).split()
    total_minutes = (int(h) * 60) + int(m)
    print (1440 - total_minutes)
