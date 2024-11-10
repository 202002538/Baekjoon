import sys
input = sys.stdin.readline
from collections import deque

if __name__ == '__main__':
    n, m, v = map(int, input().split())
    graph = [[] for _ in range(n+1)]

    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    def dfs(start):
        q = deque([start])
        result = []
        while q:
            now = q.pop()
            if now not in result:
                result.append(now)
                q.extend(sorted(graph[now], reverse=True))
        return result

    def bfs(start):
        result = []
        visited = [0] * (n + 1)
        q = deque([start])
        while q:
            now = q.popleft()
            if visited[now]:
                continue
            visited[now] = 1
            result.append(now)
            for g in sorted(graph[now]):
                q.append(g)
        return result

    print(*dfs(v))
    print(*bfs(v))