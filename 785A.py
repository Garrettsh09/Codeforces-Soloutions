x = int(input())
count = 0
for i in range(x):
    y = str(input())
    if y == 'Icosahedron':
        count += 20
    elif y == 'Dodecahedron':
        count += 12
    elif y == 'Octahedron':
        count += 8
    elif y == 'Cube':
        count += 6
    elif y == 'Tetrahedron':
        count += 4
print (count)