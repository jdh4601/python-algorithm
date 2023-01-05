from ssearch_while import seq_search

print('*' * 20)
print('실수를 검색합니다 (end 시 종료)')

number = 0
x = []

while True:
    s = input(f'x[{number}]: ')
    if s == 'end' or s == 'End':
        break
    x.append(float(s))
    number += 1

key = float(input('검색할 값을 입력하시오: '))

idx = seq_search(x, key)

if idx == -1:
    print('원소 존재 x')
else:
    print(f'검색 값은 x[{idx}]에 있음')
