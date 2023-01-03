counter = 0

for n in range(2, 101):
    for i in range(2, n):
        counter += 1
        if n % i == 0:  # 나누어 떨어짐 -> 소수 아님
            break
    else:
        print(n)

print(counter)  # counter : 1133번 실행됨 -> 개선 필요
