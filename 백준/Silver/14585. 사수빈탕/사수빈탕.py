import sys
input = sys.stdin.readline

if __name__ == '__main__':
    n, m = map(int, input().split())
    candy = []
    max_x, max_y = 0, 0
    for _ in range(n):
        x, y = map(int, input().split())
        max_x, max_y = max(max_x, x), max(max_y, y)
        candy.append((x, y))

    dp = [[0] * (max_x+1) for _ in range(max_y+1)]
    for i in range(max_y+1):
        for j in range(max_x+1):
            dp[i][j] = max(dp[max(0, i-1)][j], dp[i][max(0, j-1)])
            if (i, j) in candy:
                dp[i][j] += max(0, m-(i+j))
    print(dp[max_y][max_x])