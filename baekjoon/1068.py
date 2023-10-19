import sys
input = sys.stdin.readline

def dfs(num, arr):
    arr[num] = -2
    for i in range(len(arr)):
        if num == arr[i]:
            dfs(i, arr)

n = int(input())
arr = list(map(int, input().split()))
k = int(input())
count = 0

dfs(k, arr)
count = 0
for i in range(len(arr)):
    if arr[i] != -2 and i not in arr:
        count += 1
print(count)


"""
import sys
read = sys.stdin.readline
sys.setrecursionlimit(10**9)

def DFS(v):
    leaves = graph[v]
    removed[v] = 0

    if leaves != []:
        for l in leaves:
            DFS(l)
        graph[v] = []


N = int(read())
graph = [[] for _ in range(N)]
root = -1
# a = list(map(int, read().split()))

for idx, p in enumerate(list(map(int, read().split()))):
    if p == -1:
        root = idx
    else:
        graph[p].append(idx)

r = int(read()) # 지우는 노드
cnt = 0

removed = [1] * N
if r == root:
    print(0)
else:
    DFS(r)

    if sum(removed) == 1:
        print(1)
    else:
        print(graph)
        print(removed)
        for idx, leaf in enumerate(graph):
            if removed[idx] == 1 and leaf == []:
                cnt += 1

        print(cnt)
"""