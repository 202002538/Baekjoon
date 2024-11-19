import sys
input = sys.stdin.readline

n, k = map(int, input().split())
burger = list(input()[:-1])
result = 0

for i, ham in enumerate(burger):
    if ham == 'P':
        for j in range(i-k, i+k+1):
            if j < 0 or j > n-1 or i == j:
                continue
            if burger[j] == 'H':
                burger[j] = 'E'
                result += 1
                break
print(result)