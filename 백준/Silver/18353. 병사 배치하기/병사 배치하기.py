import sys
input = sys.stdin.readline

if __name__ == '__main__':
    n = int(input())
    power = list(map(int, input().split()))

    dp = [1] * n

    for i in range(1, n):
        for j in range(i):
            if power[i] < power[j]:
                dp[i] = max(dp[i], dp[j]+1)
    print(n - max(dp))