import sys
input = sys.stdin.readline

if __name__ == '__main__':
    n, m = map(int, input().split())
    graph = [[] for _ in range(n)]
    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)

    dp = [1] * (n+1)

    for i in range(1, n):
        for j in graph[i]:
            dp[j] = max(dp[j], dp[i] + 1)

    print(*dp[1:])