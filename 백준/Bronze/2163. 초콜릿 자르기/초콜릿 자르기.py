a, b = map(int, input().split())
if b < a:
    a, b = b, a

print(a - 1 + a * (b-1))