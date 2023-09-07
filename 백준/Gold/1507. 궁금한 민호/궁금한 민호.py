import sys
input = sys.stdin.readline
INF = int(1e9)

if __name__ == '__main__':
    n = int(input())
    graph = []
    summ = []
    for _ in range(n):
        row = list(map(int, input().split()))
        graph.append(row)
        summ.append(row.copy())

    result = 0
    for a in range(n):
        for b in range(n):
            for k in range(n):
                if graph[a][k] + graph[k][b] == graph[a][b]:
                    # a -> b를 갈때 k를 경유한다
                    if a != b and b != k and a != k:
                        summ[a][b] = 0 #경유해서 만들어진 값은 삭제
                elif graph[a][k] + graph[k][b] < graph[a][b]:
                    result = -1

    if result != -1:
        result = 0
        for i in range(n):
            result += sum(summ[i])
        print(result // 2)
    else:
        print(result)