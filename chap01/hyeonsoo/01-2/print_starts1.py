n = int(input("n입력"))

w = int(input("w입력"))

for i in range(n):
    print('*', end='')
    if i % w == w - 1:
        print()

if n % w:
    print()