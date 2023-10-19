if __name__ == '__main__':
    receipt = int(input())
    cnt = int(input())
    
    check = 0
    for c in range(cnt):
        price, n = map(int, input().split())

        check += (price * n)
    
    if receipt == check:
        print('Yes')
    else:
        print('No')
