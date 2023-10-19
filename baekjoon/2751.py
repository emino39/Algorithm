if __name__ == '__main__':
    N = int(input())

    numbers = []

    for n in range(N):
        numbers.append(int(input()))
    
    numbers = sorted(numbers, reverse=False)

    for num in numbers:
        print(num)