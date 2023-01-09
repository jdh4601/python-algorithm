from enum import Enum
from fixed_stack import FixedStack

Menu = Enum('Menu', ['Push', 'Pop', 'Peek', 'Search', 'Dump', 'Exit'])


def select_menu():
    s = [f'({m.value}) {m.name}' for m in Menu]
    while True:
        print(*s, sep='   ', end="")
        n = int(input(':  '))
        if 1 <= n <= len(Menu):
            return Menu(n)


s = FixedStack(64)  # capacity: 64 스택

while True:
    print(f'데이터 개수: {len(s)} / {s.capacity}')
    menu = select_menu()

    if menu == Menu.Push:
        x = int(input('데이터를 입력하세요: '))
        try:
            s.push(x)
        except FixedStack.Full:
            print('stack is full')

    elif menu == Menu.Pop:
        try:
            x = s.pop()
            print(f'pop한 데이터는 {x}이다.')
        except FixedStack.Empty:
            print('stack is empty.')

    elif menu == Menu.Search:
        x = int(input('검색할 값을 입력하시오: '))
        if x in s:
            print(f'{s.count(x)}개 포함되고, 맨 앞의 위치는 {s.find(x)}')
        else:
            print('겁색값 찾을 수 없음')

    elif menu == Menu.Dump:
        s.dump()

    else:
        break
