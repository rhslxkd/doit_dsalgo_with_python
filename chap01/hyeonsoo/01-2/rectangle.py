
rectangle = int(input("직사각형 넓이"))

for i in range(1, rectangle + 1):
    if i * i > rectangle: break
    if rectangle % i: continue
    print(f'{i} * {rectangle // i}')