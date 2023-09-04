import sys
input = sys.stdin.readline
INF = int(1e9)

if __name__ == '__main__':
    n, k = map(int, input().split())

    #2차원 리스트 세팅
    graph = [[INF] * (n+1) for _ in range(n+1)]
    for a in range(n+1):
        graph[a][a] = 0
    for _ in range(k):
        a, b = map(int, input().split())
        graph[a][b] = 1
        graph[b][a] = -1

    #플로이드 워셜
    for k in range(1, n+1):
        for a in range(1, n+1):
            for b in range(1, n+1):
                if graph[a][k] == -1 and graph[k][b] == -1: #음수는 음수끼리
                    graph[a][b] = -1
                elif graph[a][k] == 1 and graph[k][b] == 1: #양수는 양수끼리
                    graph[a][b] = 1

    #알고싶은 사건 전후관계 출력
    result = []
    case = int(input())
    for _ in range(case):
        a, b = map(int, input().split())
        if graph[a][b] == INF:
            result.append(0)
        else:
            result.append(-graph[a][b])

    for r in result:
        print(r)