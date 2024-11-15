import sys
input = sys.stdin.readline

n = int(input())
nums = []
for _ in range(n):
    nums.append(int(input()))

increase = [1] * (n+1)
for i in range(1, n):
    for j in range(i):
        if nums[j] < nums[i]:
            increase[i] = max(increase[i], increase[j]+1)

print(n - max(increase))