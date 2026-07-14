from typing import Any, Sequence

def seq_seqeunce(a: Sequence, key:Any) -> int:
    for i in range(len(a)):
        if a[i] == key:
            return i
    return -1


if __name__ == '__main__':
    num = int(input("원소 수를 입력하세요:"))
    x = [None] * num

    for i in range(num):
        x[i] = int(input(f'x[{i}]: '))

    ky = int(input('검색할 값을 입력'))

    idx = seq_seqeunce(x, ky)

    if idx == -1:
          print("검색하려고 하는 원소가 존재하지 않아요")
        
    else:
        print(f'검색하시려 하는 값은 x[{idx}]에 있습니다')