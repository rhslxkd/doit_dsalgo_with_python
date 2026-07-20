# 세 정수를 입력받아 중앙값 구하기 2

def med3(a, b, c):
    """a, b, c의 중앙값 구하여 반환(다른 방법)"""
    if (b >= a and c <= a) or (b <= a and c >= a):
        return a
    elif (a > b and c < b) or (a < b and c > b): # a와 b의 비교를 이미 마친 상태에서 다시 비교하는 것은 비효율적임
        return b 
    return c
    
print('세 정수의 중앙값을 구합니다.')
a = int(input('정수 a의 값을 입력하세요.: '))
b = int(input('정수 b의 값을 입력하세요.: '))
c = int(input('정수 c의 값을 입력하세요.: '))

print(f'중앙값은 {med3(a, b, c)}입니다.')