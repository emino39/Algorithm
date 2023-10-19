# 최대힙, 최소힙
# 각 가방에 담을 수 있는 모든 보석을 찾을 때 최소힙
# 각 가방에 넣을 수 있는 보석 중 가장 가치가 큰 보석을 찾을 때 최대힙
# 이 문제는 가방 별로 훔칠 수 있는 보석을 최대힙을 통해 탐색
import sys
import heapq

read = sys.stdin.readline
N, K = map(int, read().split())
jews = []
for _ in range(N):
    heapq.heappush(jews, list(map(int, read().split())))
bags = [int(read()) for _ in range(K)]
bags.sort()

answer = 0
tmp_jew = []

for bag in bags:
    while jews and bag >= jews[0][0]:
        heapq.heappush(tmp_jew, -heapq.heappop(jews)[1])
    if tmp_jew:
        answer -= heapq.heappop(tmp_jew)
    elif not jews:
        break

print(answer)