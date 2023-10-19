T = int(input())

for t in range(T):
    N = int(input())

    if N <= 3:
        print(1)
    else:
        new = [0] * N
        new[0], new[1], new[2] = 1, 1, 1

        for n in range(3, N):
            new[n] = new[n-2] + new[n-3]

        print(new[-1])