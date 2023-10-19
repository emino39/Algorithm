import sys
read = sys.stdin.readline
sys.setrecursionlimit(10**9)

def DFS(v, weight):
    for a, b in graph[v]:
        if distance[a] == -1:
            distance[a] = weight + b
            DFS(a, weight + b)


N = int(read())
graph = [[] for _ in range(N+1)]

for n in range(N-1):
    p, s, w = map(int, input().split())
    graph[p].append([s, w])
    graph[s].append([p, w])

# 루트는 1
# 1번 노드에서 가장 먼 곳
distance = [-1] * (N+1)
distance[1] = 0
DFS(1, 0)

# 가장 먼 노드
start = distance.index(max(distance))
distance = [-1] * (N+1)
distance[start] = 0
DFS(start, 0)

print(max(distance))