n = int(input())
magnet = 0
count = 0
for i in range (n):
    a = int(input())
    if a != magnet:
        count += 1
        magnet = a
print (count)
    