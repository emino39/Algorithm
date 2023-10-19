sixteen = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7,
           '8': 8, '9': 9, 'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}

def change(A):
    total = 0
    for a in range(len(A)):
        total += sixteen[A[a]] * (16 ** (len(A)-a-1))
    return total

TC = int(input())

for tc in range(TC):
    N, K = map(int, input().split())
    numbers = list(input())
    change_num = []
    password = []

    for n in range(N//4+1):
        numbers = numbers[1:len(numbers)] + numbers[0:1]
        for i in range(4):
            num = change(numbers[(N//4)*i:(N//4)*(i+1)])
            if num not in password:
                password.append(num)

    password = sorted(password, reverse=True)

    print("#{} {}".format(tc+1, password[K-1]))