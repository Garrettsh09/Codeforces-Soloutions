n = str(input())
if int(n) >= 0:
    print (n)
else:
    if int(n[-1]) >= int(n[-2]):
        if int(n[:-1]) == 0:
            print ('0')
        else:
            print (n[:-1])
    else:
        if int(n[:-2] + n[-1]) == 0:
            print('0')
        else:
            print (n[:-2] + n[-1])