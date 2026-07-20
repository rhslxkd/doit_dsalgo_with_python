from typing import Any, Sequence
import copy

def seq_seqenc(seq: Sequence, key: Any) -> int:
    """시퀀스 seq에서 key와 일치하는 원소를 선형검색(보초법)"""

    a = copy.deepcopy(seq)
    a.append(key)

    i = 0
    while True:
        if a[i] == key:
            break
        i += 1
    return -1 if i == len(seq) else i
if __name__ == '__main__':
    num = int(input("원소 수를 입력하시오"))
    x = [None] * num

    for i in range(num):
        x[i] = int(input(f'x[{i}]'))
    ky = int(input('key값을 입력'))

    idx = seq_seqenc(x, ky)

    if idx == -1:
        print('검색값을 갖는 원소가 없다잉')
    else:
        print(f'찾으시는 값은 x[{idx}]에 이씅ㅁ')