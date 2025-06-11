import sys
input = sys.stdin.readline

# 평점을 정수(×100)로 매핑
level = {
    'A+': 450, 'A0': 400, 'B+': 350, 'B0': 300,
    'C+': 250, 'C0': 200, 'D+': 150, 'D0': 100,
    'F':    0
}
llist = ['F', 'D0', 'D+', 'C0', 'C+', 'B0', 'B+', 'A0', 'A+']

# n, x 읽어서 x도 정수(×100)로 변환
n_str, x_str = input().split()
n = int(float(n_str))
if '.' in x_str:
    w, f = x_str.split('.')
    x = int(w) * 100 + int((f + '00')[:2])
else:
    x = int(x_str) * 100

grade = 0
score = 0
for _ in range(n - 1):
    g, s = input().split()
    grade += int(g)
    score += level[s] * int(g)
last = int(input())
grade += last

# 남은 한 과목 등급별로 확인
for g in llist:
    total = score + level[g] * last
    # (평균 × 1000)을 내림
    tmp = total * 10 // grade
    # (평균 × 100)을 내림
    final = tmp // 10
    if final > x:
        print(g)
        break
else:
    print("impossible")