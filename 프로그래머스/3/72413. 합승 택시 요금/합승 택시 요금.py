INF= 1e9
import sys
input = sys.stdin.readline

def solution(n, s, a, b, fares):
    graph = [[INF] * (n+1) for _ in range(n+1)]

    for i in range(1, n+1):
        graph[i][i] = 0

    for i, j, d in fares:
        graph[i][j] = d 
        graph[j][i] = d

    #플로이드 워셜
    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

    result = INF
    for i in range(1, n+1):
        tmp = 0
        tmp += graph[s][i]
        tmp += graph[i][a]
        tmp += graph[i][b]
        result = min(result, tmp)
    return result