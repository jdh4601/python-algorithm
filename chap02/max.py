# 시퀀스 원소의 최댓값 구하기
from typing import Any, Sequence


def max_of(a: Sequence) -> Any:
    maximum = a[0]
    for i in range(1, len(a)):
        if a[i] > maximum:
            maximum = a[i]
    return maximum


# 직접 실행될 때만 실행되고 임포트될 때는 실행되지 않음
if __name__ == '__main__':
    print("배열의 최댓값을 구합니다")
    num = int(input('원소 수 입력 : '))
    x = [None] * num  # 배열 요소 개수 결정

    for i in range(num):
        x[i] = int(input(f'x[{i}]값을 입력하세요 : '))

    print(f'최댓값은 {max_of(x)}입니다.')
