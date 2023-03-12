t = int(input())
a = list(input())

print(a)
res = [a[i: j] for i in range(len(a))
    for j in range(i + 1, len(a) + 1)]

longest = 0
for i in res:
    if list(i) == sorted(i):
        if len(i) > longest:
            longest = len(i)

print (longest)