# def sum1_ton(n):
#     sum = 0
#     while n > 0:
#         sum += n
#         n -= 1
#     return sum


# x = int(input("x를 입력 : "))
# print(f'1부터 {x}까지의 합은 {sum1_ton(x)}입니다')

def change(lst, idx, val):
    lst[idx] = val


x = [11, 22, 33, 44, 55]
print('x = ', x)

index = int(input('enter an index : '))
value = int(input('enter a value : '))

change(x, index, value)  # 실제 값의 참조가 change의 매개변수로 전달됨
print(f'x = {x}')
