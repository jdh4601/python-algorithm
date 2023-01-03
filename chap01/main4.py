n = int(input("변의 길이? : "))

# for i in range(n):
#     for j in range(i + 1):
#         print('*', end="")
#     print()

for i in range(n):
    for _ in range(n - i - 1):  # 공백 출력
        print(' ', end="")
    for _ in range(i + 1):
        print('*', end="")
    print()
