if __name__ == '__main__':
    N = int(input())

    cnt = 0
    number = 0

    while True:
        if cnt == N:
            break
        
        number += 1

        if '666' in str(number):
            cnt += 1

    print(number)