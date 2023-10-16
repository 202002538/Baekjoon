import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

if __name__ == '__main__':
    n, m, r = map(int, input().split())
    graph = [[] for _ in range(n+1)]
    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    visited = [-1] * (n+1) #깊이
    order = [0] * (n+1) #방문순서
    visited[r] = 1

    o = 1
    def dfs(r, depth):
        global o
        visited[r] = depth
        order[r] = o

        graph[r].sort(reverse=True)
        for e in graph[r]:
            if visited[e] == -1:
                o += 1
                dfs(e, depth+1)
    dfs(r, 0)

    result = 0
    for i in range(1, n+1):
        result += order[i] * visited[i]
    print(result)