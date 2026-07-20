a = int(input('a 입력'))
b = int(input('b 입력'))

if a > b:
    a, b = b, a 

sum = 0
for i in range(a, b + 1):
    sum += i

print(f"{a}~{b}까지 합은 {sum}")