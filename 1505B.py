a = str(input())
if len(str(a)) <= 2:
    count = 0
    for i in a:
        count += int(i)
    print (count)
else:
    while len(str(a)) > 1:
        count = 0
        for i in str(count):
            count += int(i)
    print (count)