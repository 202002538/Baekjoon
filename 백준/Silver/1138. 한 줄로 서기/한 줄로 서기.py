import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))

original = [i for i in range(1, n+1)] 
for i in range(n-1, -1, -1):
    now = original.pop(i)
    original.insert(i+nums[i], now)
print(*original)