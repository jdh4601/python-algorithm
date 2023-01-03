# 구구단 곱셈표

while True:
    n = int(input("몇단 까지? : "))
    if n > 0:
        print("-" * 35)

        for i in range(1, n+1):
            for j in range(1, 10):
                print(f'{i * j:3}', end=" ")
            print()

        print('-' * 35)

        break
