N = int(input())
distance = list(map(int, input().split()))
costs = list(map(int, input().split()))

total = costs[0] * distance[0]
before_cost = costs[0]

for n in range(1, N-1):
    if before_cost * distance[n] > costs[n] * distance[n]:
        total += costs[n] * distance[n]
        before_cost = costs[n]
    else:
        total += before_cost * distance[n]

print(total)