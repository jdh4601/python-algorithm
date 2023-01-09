# 링 버퍼로 큐 만들기

class FixedQueue:
    class Empty(Exception):
        pass

    class Full(Exception):
        pass

    # 초기화 함수
    def __init__(self, capacity) -> None:
        self.no = 0  # 데이터 개수
        self.front = 0  # 맨앞 인덱스
        self.rear = 0  # 맨뒤 인덱스
        self.capacity = capacity  # 큐의 크기
        self.que = [None] * capacity  # 리스트형 배열, 큐의 본체

    # 추가한 데이터 개수 파악
    def __len__(self) -> int:
        return self.no

    def is_empty(self) -> bool:
        return self.no <= 0

    def is_full(self) -> bool:
        return self.no >= self.capacity

    # 데이터 추가 함수 (x를 인큐)
    def enque(self, x):
        if self.is_full():  # 큐가 가득 차면? 에러 발생
            raise FixedQueue.Full
        self.que[self.rear] = x  # 맨뒤에 x를 넣기
        self.rear += 1  # rear값 1 추가
        self.no += 1  # 원소 수 1 추가
        # rear값이 배열의 맨 끝값이라면?
        if self.rear == self.capacity:
            self.rear = 0

    # 데이터 꺼내기
    def deque(self):
        if self.is_empty():
            raise FixedQueue.Empty
        x = self.que[self.front]  # 0에서 시작
        self.front += 1
        self.no -= 1
        if self.front == self.capacity:
            self.front = 0
        return x  # 1만큼 더해진 front값의 큐

    # front 값을 반환함
    def peek(self):
        if self.is_empty():
            raise FixedQueue.Empty
        return self.que[self.front]

    # value와 같은 데이터 위치 찾음
    def find(self, value):
        for i in range(self.no):
            idx = (i + self.front) % self.capacity
            if self.que[idx] == value:
                return idx
        return -1

    # 큐 안의 value 데이터 개수 세기
    def count(self, value):
        c = 0
        for i in range(self.no):
            idx = (i + self.front) % self.capacity
            if self.que[idx] == value:
                c += 1
        return c

    def __contains__(self, value):
        return self.count(value)

    # 큐의 전체 원소 삭제
    def clear(self) -> None:
        self.no = self.front = self.rear = 0

    def dump(self) -> None:
        if self.is_empty():
            print('큐가 비었습니다')
        else:
            # front부터 끝까지 순서대로 출력
            for i in range(self.no):
                print(self.que[(i + self.front) % self.capacity], end=" ")
                print()
