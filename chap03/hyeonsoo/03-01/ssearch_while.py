from typing import Any, Sequence

def deq_dequence(a: Sequence, key: Any) -> Any:
    """시퀀스 a에서 key와 값이 같은 원소를 선형 검색(while문)"""

    i = 0

    while True:
        if i == len(a):
            return -1 #검색에 실패하면 -1을 반환
        if a[i] == key:
            return i
        i += 1

if __name__ == '__main__':
    num = int(input("원소 수를 입력하세요:"))
    x = [None] * num

    for i in range(num):
        x[i] = int(input(f'x[{i}]: '))

    ky = int(input('검색할 값을 입력'))

    idx = deq_dequence(x, ky)

    if idx == -1:
          print("검색하려고 하는 원소가 존재하지 않아요")
        
    else:
        print(f'검색하시려 하는 값은 x[{idx}]에 있습니다')