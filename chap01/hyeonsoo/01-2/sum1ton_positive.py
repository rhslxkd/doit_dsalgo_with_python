while True:
    n = int(input("값 입력"))
    if n > 0:
        break

sum = 0
i = 1

for i in range(1, n + 1):
    sum += i
    i += 1

print(f"1~{n}합은 {sum}")