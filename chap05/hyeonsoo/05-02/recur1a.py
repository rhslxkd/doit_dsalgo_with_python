def recur(n: int) -> int:
    """꼬리 재귀를 제거한 recur() 함수"""
    while n > 0:
        recur(n - 1)
        print(n)
        n = n - 2

x = int(input('값을 입력하시오'))

recur(x)