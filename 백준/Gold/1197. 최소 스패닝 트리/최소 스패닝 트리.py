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
    v, e = map(int, input().split())
    edges = []
    for _ in range(e):
        a, b, c = map(int, input().split())
        edges.append((c, a, b))

    edges.sort()

    #크루스칼
    result = 0
    parent = [i for i in range(v+1)]
    for edge in edges:
        c, a, b = edge
        if find(parent, a) != find(parent, b):
            union(parent, a, b)
            result += c

    print(result)