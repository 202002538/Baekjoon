import sys
input = sys.stdin.readline
INF = int(1e9)

if __name__ == '__main__':
    n = int(input())
    m = int(input())

    #최단거리 저장 리스트 세팅
    graph = [[INF] * (n+1) for _ in range(n+1)]
    for a in range(n+1):
        graph[a][a] = 0
    for _ in range(m):
        a, b, c = map(int, input().split())
        graph[a][b] = min(graph[a][b], c) #노선이 여러개일 수 있음

    #플로이드 워셜
    for k in range(1, n+1):
        for a in range(1, n+1):
            for b in range(1, n+1):
                graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])

    #출력
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            if graph[a][b] == INF:  # 도달할 수 없는 경우
                print("0", end=" ")
            else:
                print(graph[a][b], end=" ")
        print()