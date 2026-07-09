from typing import Any, Sequence

def max_of(a: Sequence) -> Any: 
    # 어노테이션
    # a: Sequence -- 매개변수 어노테이션: "a는 Sequence 타입이야."
    # -> Any --  반환값 어노테이션: "이 함수가 돌려주는 값은 Any(아무타입)야."
    """시퀀스형 a 원소의 최댓값을 반환""" 
    # 독스트링(docstring)
    # print(max_of.__doc__) -> 위의 문장이 출력됨
    # help(max_of) -> 함수 설명 문서로 보여줌 -> 코드 리뷰할때 도움 되겠다.

    maximum = a[0]

    for i in range(1, len(a)):
        if a[i] > maximum: maximum = a[i]

    return maximum

if __name__ == '__main__':
    print("배열의 최댓값을 구합니다.")
    num = int(input('원소 수를 입력하세요'))
    x = [None] * num

    for i in range(num):
        x[i] = int(input(f'x[{i}]값을 입력하세요.:'))

    print(f'최댓값은 {max_of(x)}입니다.')