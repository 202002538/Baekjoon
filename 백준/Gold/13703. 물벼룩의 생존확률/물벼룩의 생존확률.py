import sys
input = sys.stdin.readline

if __name__ == '__main__':
    depth, n = map(int, input().split())
    dp = [[0] * (depth+n+1) for _ in range(n+1)] #행:시간/ 열:깊이
    dp[0][depth] = 1 #시작 깊이 저장

    for i in range(n):
        for j in range(1, depth+n+1):
            if dp[i][j]:
                if i+1 < depth+n+1:
                    if 0 <= j-1:
                        dp[i+1][j-1] += dp[i][j]
                    if j+1 < depth+n+1:
                        dp[i + 1][j + 1] += dp[i][j]

    print(sum(dp[-1][1:]))