t = int(input())

for i in range(t):
    s = str(input())
    if s in ["YES", "yES", "yes", "Yes", "YeS","yEs", 'YEs',"yeS"]:
        print ('YES')
    else:
        print ('NO')