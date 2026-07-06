def median(a, b, c):
    if (a <= b and a >= c) or (a >= b and a <= c):
        return a
    elif (b >= c and b <= a) or (b >=a and b <=c):
        return b
    else:
        return c
    
print("세 정수의 중앙값을 구할게여")
a = int(input("정수 a의 값을 입력하세요.:"))
b = int(input("정수 b의 값을 입력하세요.:"))
c = int(input("정수 c의 값을 입력하세요.:"))

print(f"세 정수의 중앙값은: {median(a, b, c)}")

# 중복비교, (비효율적): 전의 코드는 한번 비교한 값을 저장중.