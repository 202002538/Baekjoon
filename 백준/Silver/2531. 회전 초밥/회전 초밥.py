import sys
input = sys.stdin.readline

n, d, k, c = map(int, input().split())
sushi = []
for _ in range(n):
    sushi.append(int(input()))
sushi.extend(sushi)

result = 0
for i in range(n+1):
    eat = set(sushi[i:i+k].copy())
    eat.add(c)
    result = max(result, len(eat))

    if result == d:
        break

print(result)