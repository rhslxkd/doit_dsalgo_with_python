n = int(input("n"))
w = int(input("w"))

for _ in range(n//w):
    print("*" * w)

rest = n % w
if rest:
    print('*' * rest)