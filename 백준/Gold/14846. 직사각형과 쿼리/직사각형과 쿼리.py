import sys
input = sys.stdin.readline

if __name__ == '__main__':
    n = int(input())
    matrix = []
    for _ in range(n):
        matrix.append(list(map(int, input().split())))

    dp = [[[0] * 11 for _ in range(n+1)] for _ in range(n+1)]
    for i in range(1, n+1):
        for j in range(1, n+1):
            for k in range(1, 11):
                dp[i][j][k] = dp[i-1][j][k] + dp[i][j-1][k] - dp[i-1][j-1][k]
            dp[i][j][matrix[i-1][j-1]] += 1

    q = int(input())
    for _ in range(q):
        x1, y1, x2, y2 = map(int, input().split())
        result = 0
        for k in range(1, 11):
            if dp[x2][y2][k] - dp[x2][y1-1][k] - dp[x1-1][y2][k] + dp[x1-1][y1-1][k] >= 1:
                result += 1
        print(result)