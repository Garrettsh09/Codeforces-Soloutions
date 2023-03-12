x = int(input())
count = 0
for i in range(1, x):
    if x <= 2:
        count += 0.5
    elif (x - int(i)) % int(i) == 0:
        count += 1
if count == 0.5:
    print ('1')
else:
    print (int(count))