import sys
input = sys.stdin.readline

if __name__ == '__main__':
    n, m = map(int, input().split())
    nums = []
    for _ in range(n):
        nums.append(int(input()))
    nums.sort()

    start = 0
    end = 1
    result = nums[-1] - nums[0]

    while start <= end <= n-1:
        now = nums[end] - nums[start]

        if now >= m:
            result = min(result, now)
            start += 1
        else:
            end += 1
    print(result)