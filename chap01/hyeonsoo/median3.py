# 세 정수의 중간값 구하기

def median(a, b, c):
    if a >= b:
        if b >= c:
            return b
        elif a <= c:
            return a
        else:
            return c
    elif c < a:
        return a
    elif c > b:
        return b
    else:
        return c
    
print("세 정수의 중앙값을 구할게여")
a = int(input("정수 a의 값을 입력하세요.:"))
b = int(input("정수 b의 값을 입력하세요.:"))
c = int(input("정수 c의 값을 입력하세요.:"))

print(f"세 정수의 중앙값은: {median(a, b, c)}")