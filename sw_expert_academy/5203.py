def check_triplet(card_dict):
    for v in card_dict.values():
        if v == 3:
            return True
    return False

def check_run(card_dict):
    runs = [
        [0, 1, 2], [1, 2, 3], [2, 3, 4], [3, 4, 5],
        [4, 5, 6], [5, 6, 7], [6, 7, 8], [7, 8, 9]
    ]
    card_nums = [k for k, v in card_dict.items() if v >= 1]
    if len(card_nums) < 3:
        return False
    else:
        for c in range(len(card_nums) - 2):
            if card_nums[c:c+3] in runs:
                return True
        return False

TC = int(input())

for tc in range(TC):
    cards = list(map(int, input().split()))
    first, second = dict(), dict()
    flag = 0 # 0 무승부, 1 1승리, 2 2승리
    for i in range(10):
        first.setdefault(i, 0)
        second.setdefault(i, 0)

    for i in range(12):
        # first에게 카드 주기
        if i % 2 == 0:
            first[cards[i]] += 1
            # check triplet
            if check_triplet(first):
                flag = 1
                break
            # check run
            if check_run(first):
                flag = 1
                break
        else:
            second[cards[i]] += 1
            if check_triplet(second):
                flag = 2
                break
            if check_run(second):
                flag = 2
                break

    print('#{} {}'.format(tc+1, flag))