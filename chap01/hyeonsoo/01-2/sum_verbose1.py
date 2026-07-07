# a~b까지 과정과 출려까지

a = int(input('a입력'))
b = int(input('b입력'))

if a > b:
    b, a = a, b

sum = 0 

for i in range(a, b+1):
    if i < b:
        print(f"{i} + ", end='')
    else:
        print(f"{i} =", end='')
    sum += 1

print(sum)
