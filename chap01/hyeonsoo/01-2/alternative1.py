n = int(input("몇번 반복할까"))

for i in range(n): # i = 0,1,2,3,4,5,.....
    if i % 2:
        print('-', end='')
    else:
        print('+', end='')

print()