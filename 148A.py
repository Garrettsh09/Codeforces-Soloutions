k = int(input())
l = int(input())
m = int(input())
n = int(input())
dragons = int(input())
list = []
slimed = []
for i in range(1, dragons + 1):
    list.append(i)
for i in range(dragons):
    if list[i] % k == 0 or list[i] % l == 0 or list[i] % m == 0 or list[i] % n == 0:
        slimed.append(list[i])
print (len(slimed))