import sys
input = sys.stdin.readline
INF = 1e9

if __name__ == '__main__':
    n = int(input())
    m = int(input())
    graph = []
    for _ in range(n):
        graph.append(list(map(int, input().split())))
    trip = list(map(int, input().split()))

    for i in range(n):
        for j in range(n):
            if i == j:
                graph[i][j] = 0
            elif graph[i][j] == 0:
                graph[i][j] = INF

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if graph[i][k] + graph[k][j] < graph[i][j]:
                    graph[i][j] = graph[i][k] + graph[k][j]

    for i in range(1, m):
        if graph[trip[i - 1] - 1][trip[i] - 1] == INF:
            print("NO")
            break
    else:
        print("YES")