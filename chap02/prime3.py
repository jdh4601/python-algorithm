counter = 0
ptr = 0
prime = [None] * 100

prime[ptr] = 2  # 2는 소수
ptr += 1

prime[ptr] = 3  # 3은 소수
ptr += 1

# prime = [2, 3]

for n in range(5, 101, 2):  # 5, 7, 9 ... 홀수
    i = 1
    while prime[i] * prime[i] <= n:
        counter += 2
        if n % prime[i] == 0:  # 소수로 나누어떨어질 때? 반복문 중단
            break
        i += 1
    else:
        prime[ptr] = n
        ptr += 1
        counter += 1

for i in range(ptr):
    print(prime[i])

print(counter)  # 191 회
