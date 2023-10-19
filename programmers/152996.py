from collections import defaultdict

def solution(weights):
    answer = 0
    weight_dict = defaultdict(int)

    for weight in weights:
        weight_dict[weight] += 1

    for num, cnt in weight_dict.items():
        if cnt > 1:
            answer += cnt * (cnt - 1) // 2 # combination nC2
        
        if num * 2 in weight_dict:
            answer += cnt * weight_dict[num * 2]
        if num * 3 % 2 == 0 and num * 3 // 2 in weight_dict:
            answer += cnt * weight_dict[num * 3 // 2]
        if num * 4 % 3 == 0 and num * 4 // 3 in weight_dict:
            answer += cnt * weight_dict[num * 4 // 3]

    return answer