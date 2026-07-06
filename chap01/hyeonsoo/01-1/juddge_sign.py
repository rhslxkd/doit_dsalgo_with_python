# 입력받은 정수의 부호(양수, 음수, 0) 출력하기

n = int(input('정수를 입력하세요:'))

if n > 0:
    print("n은 양수")
elif n < 0:
    print("n은 음수")
else:
    print("n은 0")