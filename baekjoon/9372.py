import sys
read = sys.stdin.readline

T = int(read())

for t in range(T):
    N, M = map(int, read().split())
    # graph = [[] for _ in range(N+1)]

    for m in range(M):
        a, b = map(int, read().split())
    #     graph[a].append(b)
    #     graph[b].append(a)

    # 모든 국가를 여행하기 위해 타야하는 비행기의 종류의 최소 개수
    # => DFS라고 생각했는데 모든 국가가 연결되어있다고 하면 N-1번의 이동을 하면 된다고 함
    print(N-1)