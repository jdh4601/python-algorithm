counter = 0  # 나눗셈 횟수 카운트
ptr = 0  # 이미 찾은 소수의 개수
prime = [None] * 100  # 소수 저장하는 배열

prime[ptr] = 2  # 초깃값 2로 지정 (prime = [2])
ptr += 1  # 배열 안에 소수 2존재

for n in range(3, 101, 2):  # 홀수만 대상으로(3->5->7->9 ...)
    for i in range(1, ptr):  # 1~이미 찾은 소수 개수
        counter += 1
        if n % prime[i] == 0:  # n을 소수(2, 3, 5...)로 나눠서 나누어 떨어지면 소수 아님
            break

    else:
        prime[ptr] = n  # 홀수인 소수 n을 배열에 등록 [2, 3, 5]
        ptr += 1  # 찾은 소수 개수 1개 추가

for i in range(ptr):
    print(prime[i])

print(f'나눗셈을 실행한 횟수: {counter}')  # 313
