x = int(input())
count = 0
while (x):
    if x >= 5:
        x -= 5
        count += 1
    elif x == 4:
        x -= 4
        count += 1
    elif x == 3:
        x -= 3
        count += 1
    elif x == 2:
        x -= 2
        count += 1
    elif x == 1:
        x -= 1
        count += 1
print (count)