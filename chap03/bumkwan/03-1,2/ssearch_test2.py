# seq_search() 함수를 사용하여 특정 인덱스 검색하기

from ssearch_while import seq_search

t = (4, 7, 5.6, 2, 3.14, 1)          # 튜플 (정수+실수 섞임)
s = 'string'                          # 문자열
a = ['DTS', 'AAC', 'FLAC']            # 문자열 리스트

print(f'{t}에서 5.6의 인덱스는 {seq_search(t, 5.6)}입니다.')
print(f'{s}에서 "n"의 인덱스는 {seq_search(s, "n")}입니다.')
print(f'{a}에서 "DTS"의 인덱스는 {seq_search(a, "DTS")}입니다.')