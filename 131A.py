x = str(input())
count = 0
for i in range(1, len(x)):
    if x[i] == x[i].upper():
        count += 1
if count == len(x) - 1 and x[0] != x[0].upper():
    print (x[0].upper() + x[1:len(x)].lower())
elif count == len(x) - 1 and x[0] == x[0].upper():
    print (x.lower())
else:
    print(x)
