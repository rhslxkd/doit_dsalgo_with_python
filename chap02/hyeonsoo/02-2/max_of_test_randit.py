import random
from max import max_of

print('난수의 최댓값을 구합니다')
num = int(input("난수의 개수를 입력"))
lo = int(input("난수의 최솟값을 입력"))
hi = int(input("난수의 최댓값을 입력"))
x = [None] * num

for i in range(num):
    x[i] = random.randint(lo, hi) #lo이상 hi이하인 정수 난수를 반환

print(f'{(x)}')
print(f"이 난수가운데 최댓값은 {max_of(x)}입니다")
print(f"이 난수가운데 최댓값은 {hi}입니다")
 
 
 
 