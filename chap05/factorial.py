def factorial(n):
    if n > 0:
        return n * factorial(n-1)
    else:
        return 1


if __name__ == '__main__':
    n = int(input('출력할 값을 입력하시오: '))
    print(f'{n}! = {factorial(n)}')
