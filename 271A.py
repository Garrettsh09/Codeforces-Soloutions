y = int(input())
count = y + 1
while count:
    if len(set(str(count))) == 4:
        print (count)
        break
    else:
        count += 1
