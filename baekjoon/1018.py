if __name__ == '__main__':
    N, M = map(int, input().split())

    # 입력받은 체스판을 저장하기 위한 리스트
    board = []

    count = []

    for _ in range(N):
        board.append(input())
    
    # 체스판 자르기 위한 시작점 잡기 (n, m)
    for n in range(N-7):
        for m in range(M-7):
            cnt_w = 0
            cnt_b = 0

            # (i+j) 값이 짝수면 체스판 시작점과 같은 색이어야 하고
            # (i+j) 값이 홀수면 체스판 시작점과 다른 색이어야 함
            for i in range(n, n+8):
                for j in range(m, m+8):
                    if (i + j) % 2 == 0:
                        if board[i][j] != 'W':
                            cnt_w += 1
                        else:
                            cnt_b += 1
                    else:
                        if board[i][j] != 'B':
                            cnt_w += 1
                        else:
                            cnt_b += 1
    
            count.append(min(cnt_w, cnt_b))
    
    print(min(count))