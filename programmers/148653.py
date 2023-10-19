def solution(storey):
    answer = 0

    while storey:
        remainder = storey % 10 # 현재 자릿값
        
        if remainder > 5: # 6 ~ 9
            answer += (10 - remainder) # 10까지 남은 개수
            storey += 10

        elif remainder < 5: # 0 ~ 4
            answer += remainder # 0까지 남은 개수
        
        else: # 5, 앞 자릿값에 따라 달라짐
            if (storey // 10) % 10 > 4: # 앞 자릿값이 5 이상이면 자리 올림
                storey += 10
            answer += remainder

        storey = storey // 10

    return answer

if __name__ == "__main__":
    answer = solution(95)
    print(answer)