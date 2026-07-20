x = ['Jhon', 'George', 'Paul', 'Ringo']

for i, name in enumerate(x, 1): # index 시작을 1부터 매기기(0 건너뛰는게 아니라 그냥 0이 1)
    print(f'{i}번째 = {name}')