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
    edges = []
    for i in range(1, n):
        adjacency = list(map(int, input().split()))
        for j, adj in enumerate(adjacency):
            edges.append((adj, i, j+i+1))
    edges.sort()

    # 크루스칼로 n-1개의 간선 확인, 저장
    count = [[] for _ in range(n+1)] # 인접리스트 저장
    parent = [i for i in range(n+1)]
    connected = 0 #연결한 간선 수

    for edge in edges:
        c, a, b = edge
        # a, b 연결가능 -> 서로 인접리스트에 저장/ 합집합
        if find(parent, a) != find(parent, b):
            connected += 1
            count[a].append(b)
            count[b].append(a)
            union(parent, a, b)
        # 트리의 모든 간선 찾음
        if connected == n-1:
            break

    #출력
    for c in count[1:]:
        c.sort()
        print(len(c), *c)