N = int(input())
numbers = []

for n in range(N):
    numbers.append(int(input()))

numbers = sorted(numbers, reverse=False)
total = 0

if N == 1:
    print(total)
elif N == 2:
    print(sum(numbers))
else:
    total = numbers[0] + numbers[1]

    for n in range(2, N):
        total += (total + numbers[n])

    print(total)