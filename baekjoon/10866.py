import sys
from collections import deque

read = sys.stdin.readline

N = int(read())
arr = deque()

for _ in range(N):
    command = list(map(str, read().split()))

    if len(command) == 1:
        if command[0] == 'pop_front':
            if len(arr) != 0:
                print(arr.popleft())
            else:
                print(-1)
        elif command[0] == 'pop_back':
            if len(arr) != 0:
                print(arr.pop())
            else:
                print(-1)
        elif command[0] == 'front':
            if len(arr) != 0:
                print(arr[0])
            else:
                print(-1)
        elif command[0] == 'back':
            if len(arr) != 0:
                print(arr[-1])
            else:
                print(-1)
        elif command[0] == 'size':
            print(len(arr))
        elif command[0] == 'empty':
            if len(arr) == 0:
                print(1)
            else:
                print(0)

    else:
        if command[0] == 'push_front':
            arr.appendleft(int(command[1]))
        elif command[0] == 'push_back':
            arr.append(int(command[1]))
