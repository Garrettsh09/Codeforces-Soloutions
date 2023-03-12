import math
n = int(input())
s = str(input())
ones = s.count('1')
twos = s.count('2')
threes = s.count('3')
fours = s.count ('4')

taxis = 0
taxis += fours
if ones >= threes:
    taxis += threes
    ones -= threes
else:
    taxis += threes
    ones -= ones

if twos % 2 == 0:
    taxis += math.floor(twos/2)
else:
    taxis += math.floor(twos/2) + 1
    if ones > 2:
        ones -= 2
    else:
        ones -= ones

if ones > 0:
    taxis += math.ceil(ones/4)

print (taxis)
