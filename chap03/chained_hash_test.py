from enum import Enum
from chained_hash import ChainedHash

Menu = Enum('Menu', ['Add', 'Remove', 'Search', 'Dump', 'Exit'])


def select_menu() -> Menu:
    s = [f'[{m.value}] : {m.name}' for m in Menu]
    while True:
        print(*s, sep="  ", end='')
        n = int(input(': '))
        if 1 <= n <= len(Menu):
            return Menu(n)


hash = ChainedHash(13)  # 크기가 13인 hash table 생성

while True:
    menu = select_menu()  # 메뉴 선택

    # 추가하기
    if menu == Menu.Add:
        key = int(input('enter a key: '))
        val = input('enter a value: ')
        # if not : 조건문 실행에 실패하면 다음 줄 실행
        if not hash.add(key, val):
            print('추가를 실패했습니다')

    elif menu == Menu.Remove:
        key = int(input('enter a key: '))
        if not hash.remove(key):
            print('삭제 실패')

    elif menu == Menu.Search:
        key = int(input('enter a key: '))
        t = hash.search(key)  # 검색할 key를 값으로 받아옴
        if t is not None:
            print(f'검색한 키를 갖는 값은 {t}이다')
        else:
            print('검색할 데이터가 없습니다')

    elif menu == Menu.Dump:
        hash.dump()

    else:
        break
