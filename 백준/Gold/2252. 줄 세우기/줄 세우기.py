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
    graph = [[] for _ in range(n+1)]
    indegree = [0] * (n+1)

    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        indegree[b] += 1

    #위상정렬
    result = []
    q = deque()
    for i in range(1, n+1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()
        result.append(now)
        for j in graph[now]:
            indegree[j] -= 1
            if indegree[j] == 0:
                q.append(j)

    print(*result)