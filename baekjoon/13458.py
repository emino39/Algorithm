N = int(input())
students = list(map(int, input().split()))
B, C = map(int, input().split())

# 비트연산
ans = N # 총감독관 수만큼

for s in students:
    if s - B > 0: # 총감독관이 감독하는 인원 외의 인원은 부감독관에게 할당
        ans += (s - B + C - 1) // C

print(ans)

total = 0

for n in range(N):
    if students[n] - B > 0:
        total += 1
        students[n] -= B
        if students[n] % C == 0:
            total += (students[n] // C)
        else:
            total += (students[n] // C) + 1
    else:
        total += 1

print(total)


