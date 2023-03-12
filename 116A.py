n = int(input())
passengers = 0
most_passengers = 0
for i in range(n):
    a, b = (map(int,input().split()))
    passengers -= a
    passengers += b
    if passengers > most_passengers:
        most_passengers = passengers
print (most_passengers)