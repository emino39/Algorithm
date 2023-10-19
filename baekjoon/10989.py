import sys

if __name__ == '__main__':
    N = int(input())

    numbers = [0] * 10001

    for n in range(N):
        numbers[int(sys.stdin.readline())] += 1
    
    for i in range(10001):
        if numbers[i] != 0:
            for j in range(numbers[i]):
                print(i)
