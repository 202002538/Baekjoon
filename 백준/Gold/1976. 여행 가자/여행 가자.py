import sys
input = sys.stdin.readline

if __name__ == '__main__':
    n = int(input())
    m = int(input())
    graph = []
    for _ in range(n):
        graph.append(list(map(int, input().split())))
    trip = list(map(int, input().split()))

    def union(a, b):
        a = find(a)
        b = find(b)
        if a < b:
            parent[b] = a
        else:
            parent[a] = b

    def find(a):
        if parent[a] != a:
            parent[a] = find(parent[a])
        return parent[a]

    parent = [i for i in range(n)]
    for i in range(n):
        for j in range(n):
            if graph[i][j] == 1:
                union(i, j)

    for i in range(1, m):
        if parent[trip[i-1]-1] != parent[trip[i]-1]:
            print("NO")
            break
    else:
        print("YES")