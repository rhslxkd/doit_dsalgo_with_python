print("최댓값을 구하시오")

# int - 정수, float - 실수, complex - 복소수.(3+ 4i), str - 문자열
a = int(input('정수 a의 값을 입력하시오.'))
b = int(input('정수 b의 값을 입력하시오.'))
c = int(input('정수 c의 값을 입력하시오.'))

maximum = a

if b > maximum: maximum = b
if c > maximum: maximum = c

print(f"최댓값은 {maximum}입니다.")