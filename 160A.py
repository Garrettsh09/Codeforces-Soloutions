n = int(input())
a = list(map(int,input().split()))
amount = 0
value = 0
for i in a:
    while value < sum(a) / 2:
        value += i
        amount += 1
print (amount)

    