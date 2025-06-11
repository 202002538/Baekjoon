import sys
input = sys.stdin.readline

x1, y1, x2, y2, x3, y3 = map(int, input().split())
q = int(input())

for _ in range(q):
    x, y, t1, t2, t3 = list(map(int, input().split()))

    m1 = abs(x - x1) + abs(y - y1)
    m2 = abs(x - x2) + abs(y - y2)
    m3 = abs(x - x3) + abs(y - y3)

    time1 = ((m1 + t1 - 1) // t1) * t1
    time2 = ((m2 + t2 - 1) // t2) * t2
    time3 = ((m3 + t3 - 1) // t3) * t3

    print(min(time1, time2, time3))