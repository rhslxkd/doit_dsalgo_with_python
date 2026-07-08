print("5명의 인원 점수 집계")

a = int(input("a학생의 점수"))
b = int(input("b학생의 점수"))
c = int(input("c학생의 점수"))
d = int(input("d학생의 점수"))
e = int(input("e학생의 점수"))

score = 0
score += a
score += b
score += c
score += d
score += e

print(f"5인의 점수 합은 {score}, 평균은 {score // 5}")