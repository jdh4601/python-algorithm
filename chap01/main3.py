from re import I


while True:
    n = int(input("enter n : "))
    if n > 0:
        break

sum = 0
i = 1

for i in range(1, n + 1):
    sum += i
    i += 1

print(f'1부터 {n}까지의 합은 {sum}이다.')
