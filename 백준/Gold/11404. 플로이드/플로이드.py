import sys
input = sys.stdin.readline
INF = 1e9

if __name__ == '__main__':
    n = int(input())
    m = int(input())
    floyd = [[INF] * (n + 1) for _ in range(n + 1)]

    for i in range(n+1):
        floyd[i][i] = 0
    for _ in range(m):
        a, b, c = map(int, input().split())
        floyd[a][b] = min(floyd[a][b], c)

    for k in range(1, n+1): 
        for i in range(1, n+1):
            for j in range(1, n+1):
                if floyd[i][k] + floyd[k][j] < floyd[i][j]:
                    floyd[i][j] = floyd[i][k] + floyd[k][j]

    for i in range(1, n+1):
        for j in range(1, n+1):
            if floyd[i][j] == INF:
                print(0, end=" ")
            else:
                print(floyd[i][j], end=" ")
        print()