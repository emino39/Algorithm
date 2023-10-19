numbers = list(map(int, list(input())))

if sum(numbers) % 3 == 0:
    numbers = sorted(numbers, reverse=True)
    if numbers[-1] != 0: # 10의 배수
        print(-1)
    else:
        print(''.join(map(str, numbers)))
else:
    print(-1)