a = 0
def welfare(list):
    largest = 0
    for i in list:
        if i > largest:
            largest = i
    return largest
n = int(input())
a = list(map(int,input().split()))
present = 0
for i in a:
    present += welfare(a) - i
print(present)

