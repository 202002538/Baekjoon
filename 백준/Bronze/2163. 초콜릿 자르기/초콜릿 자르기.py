import sys
input = sys.stdin.readline

a, b = map(int, input().split())
c, d = a - 1, b - 1
if d < c:
    tmp = c
    c = d
    c = tmp

print(c + (c + 1) * d)