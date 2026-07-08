n = int(input("짧은변"))

for i in range(n): 
    for _ in range(n - i - 1):
        print(' ', end=' ')
    for _ in range(i + 1):
        print('*', end=' ')
    print()