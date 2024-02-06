import sys
input = sys.stdin.readline

if __name__ == '__main__':
    n = int(input())
    nums = list(map(int, input().split()))

    dp = [1] * n
    for i in range(1, n):
        for j in range(0, i):
            if nums[j] < nums[i]:
                dp[i] = max(dp[i], dp[j] + 1)

    dp2 = [1] * n
    for i in range(n-2, -1, -1):
        for j in range(n-1, i, -1):
            if nums[j] < nums[i]:
                dp2[i] = max(dp2[i], dp2[j] + 1)

    result = 0
    for i in range(n):
        result = max(result, dp[i] + dp2[i] - 1)
    print(result)