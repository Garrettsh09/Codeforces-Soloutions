x = int(input())
count = 0
cubes = 0
for i in range(x):
    while x > 0:
        cubes += i
        x -= i
        count += 1
print (count)