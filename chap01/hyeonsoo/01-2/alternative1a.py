n = int(input("몇개?"))

for i in range(1, n + 1): # i = 1,2,3,4,....
    if i % 2:
        print('+', end='')
    else:
        print('-', end='')

print()