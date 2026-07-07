n = int(input("몇개?"))

for i in range(1, n + 1):
    if i % 2:
        print('+', end='')
    else:
        print('-', end='')

print()