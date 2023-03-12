x, z = str(input()).split()
count = 0
for i in range(int(x)):
    y = str(input())
    if 'C' in y or  'M' in y or 'Y' in y:
        count += 1
    else:
        count += 0
if count > 0:
    print ('#Color')
else:
    print ('#Black&White')