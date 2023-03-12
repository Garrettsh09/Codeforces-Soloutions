pi = str(3141592653589793238462643383279)
t = int(input())
for i in range(t):
    count = 0
    n = str(input())
    for i in range(len(n)):
        if n[i] == pi[i]:
            count += 1
        else:
            break
    print (count)