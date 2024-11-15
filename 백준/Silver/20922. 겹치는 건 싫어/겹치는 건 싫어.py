import sys
input = sys.stdin.readline
from collections import defaultdict

n, k = map(int, input().split())
nums = list(map(int, input().split()))

result = 0
left, right = 0, 1
dic = defaultdict(int)
dic[nums[left]] += 1

while right < n:
    dic[nums[right]] += 1
    if dic[nums[right]] > k:
        while True:
            dic[nums[left]] -= 1
            if nums[left] == nums[right]:
                left += 1
                break
            left += 1
    result = max(result, right-left+1)
    right += 1

print(result)