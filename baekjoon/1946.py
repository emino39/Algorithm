import sys

read = sys.stdin.readline
T = int(read())

for t in range(T):
    N = int(read())
    scores = [list(map(int, read().split())) for _ in range(N)]
    scores = sorted(scores, key=lambda x: x[0]) # 서류 점수 순위 나열
    print(scores)
    cnt = 1 # 서류 점수 1등은 무조건 채용

    man = scores[0][1] # 서류 점수 1등인 사람의 면접 순위

    for i in range(1, N):
        if scores[i][1] < man: # 면접 순위가 더 높으면
            man = scores[i][1]
            cnt += 1

    print(cnt)