from itertools import combinations

N = int(input())
scores = [list(map(int, input().split())) for _ in range(N)]
people = list(range(N))

min_diff = 987654321 # 두 팀 점수 차이
for combination in combinations(people, int(N/2)):
    comb_score = 0
    rest_score = 0

    rest = list(set(people) - set(combination))

    for i in range(int(N/2)-1):
        for j in range(i+1, int(N/2)):
            comb_score += scores[combination[i]][combination[j]] + scores[combination[j]][combination[i]]
            rest_score += scores[rest[i]][rest[j]] + scores[rest[j]][rest[i]]

    min_diff = min(abs(comb_score - rest_score), min_diff)

print(min_diff)