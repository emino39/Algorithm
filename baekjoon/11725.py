import sys
sys.setrecursionlimit(10**9)

def DFS(v):
    global visited

    for g in graph[v]:
        if visited[g] == 0:
            visited[g] = v
            DFS(g)

N = int(sys.stdin.readline())
graph = [[] for _ in range(N+1)]

for n in range(N-1):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [0] * (N+1)

DFS(1)

for x in range(2, N+1):
    print(visited[x])