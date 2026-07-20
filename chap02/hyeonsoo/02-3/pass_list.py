def change(lst, inx, val):
    """lst[inx] 의 값을 val로 업데이트 """

    lst[inx] = val

x = [11,22,33,44,55]
print('x= ', x)

index = int(input("입력하셈 index"))
value = int(input("입력하셈 바꿀 값"))

change(x, index, value)
print(f'x =  {x}')

