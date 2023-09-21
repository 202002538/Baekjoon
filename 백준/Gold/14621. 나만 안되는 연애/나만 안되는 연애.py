import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)
from collections import deque

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
    n, m = map(int, input().split())
    gen = [0] + list(input().split())

    edges = []
    for _ in range(m):
        a, b, c = map(int, input().split())
        edges.append((c, a, b))
    edges.sort()

    #크루스칼
    result = 0
    connected = 0
    parent = [i for i in range(n+1)]
    for edge in edges:
        c, a, b = edge
        if find(parent, a) != find(parent, b) and gen[a] != gen[b]:
            result += c
            connected += 1
            union(parent, a, b)

    if connected == n-1: #모든 학교가 연결되었나?
        print(result)
    else:
        print(-1)