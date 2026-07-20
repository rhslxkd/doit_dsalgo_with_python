# 선형 검색 알고리즘(실습 3-1)을 보초법으로 수정

from typing import Any, Sequence
import copy

def seq_search(seq: Sequence, key: Any) -> int:
    """시퀀스 seq에서 key와 일치하는 원소를 선형 검색(보초법)"""
    a = copy.deepcopy(seq)   # seq를 복사
    a.append(key)            # 보초 key를 추가

    i = 0
    while True:
        if a[i] == key:      # 종료 조건 ①이 사라짐! ② 하나만 남음
            break            # 검색에 성공하면 while 문을 종료
        i += 1
    return -1 if i == len(seq) else i