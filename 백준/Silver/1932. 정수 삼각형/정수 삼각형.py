import sys
input = sys.stdin.readline
if __name__ == '__main__':
    n = int(input())
    dp = []
    for _ in range(n):
        dp.append(list(map(int, input().split())))

    for i in range(n-2, -1, -1):
        for j in range(len(dp[i])):
            dp[i][j] += max(dp[i+1][j], dp[i+1][j+1])

    print(dp[0][0])