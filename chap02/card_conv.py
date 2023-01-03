def card_conv(x, r):
    """정수 x -> r진수로 변환해서 문자열로 반환하기"""
    d = ''
    dchar = "0123456789ASABFLAKSWLMEPOBV"

    while x > 0:
        d += dchar[x % r]
        x //= r

    return d[::-1]  # 역순으로 변환하기


if __name__ == "__main__":
    print("10진수를 n진수로 변환하기")

    while True:
        while True:
            no = int(input("변환할 값: "))
            if no > 0:
                break

        while True:
            cd = int(input("몇 진수로 변환? : "))
            if 2 <= cd <= 36:
                break

        print(f'{cd}진수로는 {card_conv(no, cd)}입니다.')

        retry = input("한번 더?(y / n) : ")
        if (retry == 'N' or retry == 'n'):
            break
