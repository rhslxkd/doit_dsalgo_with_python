n = int(input('몇개'))

for _ in range(n // 2):
    print("+-", end='')

if n % 2:
    print("-", end='')

print()