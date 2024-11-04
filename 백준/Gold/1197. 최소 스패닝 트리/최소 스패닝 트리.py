import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

if __name__ == '__main__':
    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    def union(x, y):
        x = find(x)
        y = find(y)
        if x < y:
            parent[y] = x
        else:
            parent[x] = y

    v, e = map(int, input().split())
    parent = [i for i in range(v+1)]
    graph = []
    for _ in range(e):
        a, b, c = map(int, input().split())
        graph.append((c, a, b))
    graph = sorted(graph)

    total = 0
    need = v-1
    for c, a, b in graph:
        if need == 0:
            break
        if find(a) != find(b):
            total += c
            union(a, b)
            need -= 1
    print(total)