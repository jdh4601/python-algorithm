# while문을 이용한 선형 검색 알고리즘
from typing import Any, Sequence
import copy


def seq_search(seq: Sequence, key: Any) -> int:
    a = copy.deepcopy(seq)
    a.append(key)  # 보초 key를 추가

    for i in range(len(a)):
        if a[i] == key:  # 검색 성공시 바로 종료
            return i
    return -1 if len(seq) == i else i  # 검색 실패


if __name__ == '__main__':
    num = int(input('원소 수를 입력하세요: '))
    x = [None] * num

    for i in range(num):
        x[i] = int(input(f'x[{i}] = '))

    key = int(input('검색할 값을 입력하세요: '))

    idx = seq_search(x, key)

    if idx == -1:
        print('원소가 존재하지 않음')
    else:
        print(f'검색 값은 x[{idx}]에 있음')
