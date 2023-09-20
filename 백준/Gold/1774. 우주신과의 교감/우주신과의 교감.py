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
    god = []
    for i in range(1, n+1):
        a, b = map(int, input().split())
        god.append((i, a, b)) #행성번호와 좌표

    #간선 직접 계산, 저장
    edges = []
    for i in range(n):
        for j in range(i+1, n):
            edges.append(((abs(god[i][1]-god[j][1])**2 +
                           abs(god[i][2]-god[j][2])**2)**0.5, god[i][0], god[j][0]))
    edges.sort()
    
    #이미 이어진 행성 합집합
    parent = [i for i in range(n+1)]
    for _ in range(m):
        a, b = map(int, input().split())
        union(parent, a, b)

    #크루스칼
    result = 0
    for edge in edges:
        c, a, b = edge
        if find(parent, a) != find(parent, b):
            result += c
            union(parent, a, b)

    print(format(result, ".2f"))