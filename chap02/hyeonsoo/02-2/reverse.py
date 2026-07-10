from typing import Any, MutableSequence

def reverse_array(a: MutableSequence) -> None:
    """뮤터블 시퀀스 a의 원소를 역순으로 정렬"""

    n = len(a)
    for i in range(n // 2):
        a[i], a[n - i - 1] = a[n - i - 1], a[i]
    # return 안해도 되는 이유 ->Annotation이 None인 이유: 직접 원본을 수정한 것. 값의 복사본이 아니라 같은 객체를 가리키기 때문
    

if __name__ == '__main__':
    print('배열 원소를 역순으로 정렬')
    nx = int(input('원소 수를 입력'))
    x = [None] * nx

    for i in range(nx):
        x[i] = int(input(f"x[{i}]값을 입력"))
    
    reverse_array(x)

    print('배열 역순 정렬 완료')
    for i in range(nx):
        print(f'x[{i}] = {x[i]}')
    print(x)