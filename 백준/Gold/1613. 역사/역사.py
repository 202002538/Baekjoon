import sys
input = sys.stdin.readline

if __name__ == '__main__':
    n, k = map(int, input().split())

    #2차원 리스트 세팅
    graph = [[0] * (n+1) for _ in range(n+1)]
    for a in range(n+1):
        graph[a][a] = 0
    for _ in range(k):
        a, b = map(int, input().split())
        graph[a][b] = 1

    #플로이드 워셜
    for k in range(1, n+1):
        for a in range(1, n+1):
            for b in range(1, n+1):
                if graph[a][k] == 1 and graph[k][b] == 1:
                    graph[a][b] = 1

    #알고싶은 사건 전후관계 출력
    result = []
    case = int(input())
    for _ in range(case):
        a, b = map(int, input().split())
        if graph[a][b] == 1:
            result.append(-1)
        elif graph[b][a] == 1:
            result.append(1)
        else:
            result.append(0)

    for r in result:
        print(r)