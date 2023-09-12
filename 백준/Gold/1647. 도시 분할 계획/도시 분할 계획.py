import sys
input = sys.stdin.readline

if __name__ == '__main__':
    def find(parent, x):
        if parent[x] != x:
            parent[x] = find(parent, parent[x])
        return parent[x]

    def union(parent, a, b):
        a = find(parent, a)
        b = find(parent, b)
        if a > b:
            parent[a] = b
        else:
            parent[b] = a

    #입력 및 초기화
    n, m = map(int, input().split())
    parent = [i for i in range(n+1)]
    edges = []
    result = 0
    select = 0

    for _ in range(m):
        a, b, c = map(int, input().split())
        edges.append((c, a, b))
    edges.sort()

    #크루스칼 알고리즘
    for edge in edges:
        if select == n-2:
            break
        c, a, b = edge
        if find(parent, a) != find(parent, b):
            union(parent, a, b)
            result += c
            select += 1

    print(result)