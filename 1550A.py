r = int(input())
for i in range(r):
    array = []
    beautiful = []
    a = int(input())
    for i in range(a):
        array.append(i)
    for i in array:
        if i == 1 or i - 1 == 1 or i - 2 == 1 or i - 1 in beautiful or i - 2 in beautiful:
            array.remove(i)
            beautiful.append(i)
    print(len(beautiful))