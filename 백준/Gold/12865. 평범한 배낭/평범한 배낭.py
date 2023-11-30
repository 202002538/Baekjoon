import sys
input = sys.stdin.readline

if __name__ == '__main__': 
    n, k = map(int, input().split())
    goods = [()]
    for _ in range(n):
        w, v = map(int, input().split())
        goods.append((w, v))

    dp = [[0] * (k+1) for _ in range(n+1)]
    for i in range(1, n+1):
        for j in range(k+1):
            if goods[i][0] > j:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = max(dp[i-1][j], goods[i][1] + dp[i-1][j-goods[i][0]])
    print(dp[n][k])