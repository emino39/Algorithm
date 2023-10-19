### Combination ###
from itertools import combinations

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

houses = []
chickens = []
min_distance = 987654321 # 치킨집 조합과 집 사이의 최소 거리

for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            houses.append((i, j))
        elif arr[i][j] == 2:
            chickens.append((i, j))

for combination in combinations(chickens, M):
    # 치킨집 조합을 뽑았으니 각 집마다 M개의 치킨집 중에서 가장 가까운 곳을 하나 골라 => 그 치킨거리의 합이 가장 작은 경우를 선택
    # 각 집마다 치킨집과의 가장 짧은 거리
    sum_chicken = 0 # 각 집과 치킨집 조합 사이의 거리
    for house in houses:
        house_chicken = 987654321 # 각 집과 치킨집 사이의 최소 거리의 합
        for comb in combination:
            dist = abs(house[0] - comb[0]) + abs(house[1] - comb[1])
            if house_chicken > dist:
                house_chicken = dist
        sum_chicken += house_chicken

    if min_distance > sum_chicken:
        min_distance = sum_chicken

print(min_distance)