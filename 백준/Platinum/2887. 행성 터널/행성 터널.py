import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

if __name__ == '__main__':
    def find(parent, x):
        if x != parent[x]:
            parent[x] = find(parent, parent[x])
        return parent[x]

    def union(parent, a, b):
        a = find(parent, a)
        b = find(parent, b)
        if a > b:
            parent[a] = b
        else:
            parent[b] = a

    #input
    n = int(input())
    x, y, z = [], [], []
    for i in range(n):
        planet = list(map(int, input().split()))
        x.append((planet[0], i)) #좌표와 행성 번호 저장
        y.append((planet[1], i))
        z.append((planet[2], i))

    #좌표를 정렬 -> 좌표가 가까운 행성들이 붙어있게 됨
    x.sort()
    y.sort()
    z.sort()

    #간선 정보를 추출
    edges = []
    for i in range(n-1):
        # (비용, 행성i, 행성j) 저장
        # x, y, z축 각각을 선택하는 비용에 대해 따로 계산, 그 중 작은걸 골라 쓰겠다
        edges.append((x[i + 1][0] - x[i][0], x[i][1], x[i + 1][1]))
        edges.append((y[i + 1][0] - y[i][0], y[i][1], y[i + 1][1]))
        edges.append((z[i + 1][0] - z[i][0], z[i][1], z[i + 1][1]))
    edges.sort()

    #크루스칼
    result = 0
    parent = [i for i in range(n)]
    for edge in edges:
        c, a, b = edge
        if find(parent, a) != find(parent, b):
            result += c
            union(parent, a, b)

    print(result)