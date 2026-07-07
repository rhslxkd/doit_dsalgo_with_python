n = int(input("몇번 반복할까"))

for i in range(n):
    if i % 2:
        print('-', end='')
    else:
        print('+', end='')

print()