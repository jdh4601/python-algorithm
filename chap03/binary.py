def bin_search(a, key):
    pl = 0  # 맨 앞 인덱스
    pr = len(a) - 1  # 맨 뒤 인덱스

    while True:
        pc = (pl + pr) // 2  # 중앙 값 인덱스

        if a[pc] == key:  # 검색 성공
            return pc
        elif a[pc] > key:  # 검색 범위 뒤쪽으로
            pr = pc - 1
        elif a[pc] < key:  # 검색 범위 앞쪽으로
            pl = pc + 1
        if pl > pr:
            break

    return -1  # 검색 실패


if __name__ == '__main__':
    num = int(input('원소 수를 입력하시오: '))
    x = [None] * num

    print('오름 차순으로 입력')

    x[0] = int(input('x[0]: '))

    for i in range(1, num):
        while True:
            x[i] = int(input(f'x[{i}]: '))
            if x[i] >= x[i-1]:
                break

    key = int(input('검색할 값을 입력하시오: '))
    idx = bin_search(x, key)

    if idx == -1:
        print('존재하지 않습니다')
    else:
        print(f'검색값은 x[{idx}]에 존재.')
