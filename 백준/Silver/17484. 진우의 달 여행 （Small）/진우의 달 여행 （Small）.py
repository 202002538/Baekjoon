import sys
input = sys.stdin.readline
INF= 1e9

n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

dp = [[[i, i, i] for i in graph[0]]] + \
     [[[INF, INF, INF] for _ in range(m)] for _ in range(n-1)]

for i in range(1, n):
    for j in range(m):
        if j < m-1: #젤 오른쪽줄이 아님
            dp[i][j][0] = min(dp[i-1][j+1][1], dp[i-1][j+1][2]) + graph[i][j]
        if 0 < j: #젤 왼쪽줄이 아님
            dp[i][j][2] = min(dp[i-1][j-1][0], dp[i-1][j-1][1]) + graph[i][j]
        dp[i][j][1] = min(dp[i-1][j][0], dp[i-1][j][2]) + graph[i][j]

result = INF
for tmp in dp[-1]:
    for t in tmp:
        result = min(result, t)
print(result)