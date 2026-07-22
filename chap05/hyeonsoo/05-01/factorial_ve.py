def factorial(n: int) -> int:
    """양의 정수 n의 팩토리얼값을 재귀적으로 구함"""
    if n > 0:
        return n * factorial(n - 1)
    elif n == 0:
        return 1
    else:
        raise ValueError

if __name__ == '__main__':
    n = int(input('정수 n의 값을 입력'))
    try:
        print(f'정수{n}의 값은 {factorial(n)}입니다.')
    except ValueError:
        print('음의 정수라 안됩니다.')
        