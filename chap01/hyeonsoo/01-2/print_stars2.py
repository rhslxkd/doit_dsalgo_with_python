n = int(input("n")) # 10
w = int(input("w")) # 3

for _ in range(n//w): # 3
    print("*" * w) # 9개

rest = n % w
if rest:
    print('*' * rest)