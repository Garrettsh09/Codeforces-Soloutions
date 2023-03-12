n, m = (map(int,input().split()))
count = 0
prime_numbers = [2, 3, 5, 7 ,11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
if m not in prime_numbers:
    print ('NO')
else:
    for i in range(len(prime_numbers)):
        while n == prime_numbers[i]:
            if m == prime_numbers[i + 1]:
                print ('YES')
                break
            else:
                print ('NO')
                break