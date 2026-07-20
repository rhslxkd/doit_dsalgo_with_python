n = int(input("짧은 변의 길이"))

for i in range(n):
    for j in range(i + 1):
        print('*', end='')
    print()