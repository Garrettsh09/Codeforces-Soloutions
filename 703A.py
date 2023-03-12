x = int(input())
Mishka = 0
Chris = 0
for i in range (x):
    a, b = str(input()).split()
    if int(a) > int(b):
        Mishka += 1
    elif int(a) < int(b):
        Chris += 1
if Mishka > Chris:
    print ('Mishka')
elif Mishka < Chris:
    print ('Chris')
elif Mishka == Chris:
    print ('Friendship is magic!^^')