import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)

if __name__ == '__main__':
    n, r = map(int, input().split())
    graph = [[] for _ in range(n+1)]
    for _ in range(n-1):
        a, b, d = map(int, input().split())
        graph[a].append((b, d))
        graph[b].append((a, d))

    def wood(now, length):
        if len(graph[now]) == 1:
            b, d = graph[now].pop()
            graph[b].remove((now, d))
            return wood(b, length+d)
        else:
            return now, length

    branch_len = 0
    def branch(now, length):
        global branch_len
        if len(graph[now]) == 0:
            branch_len = max(branch_len, length)
        else:
            for b, d in graph[now]:
                graph[b].remove((now, d))
                branch(b, length+d)

    #길이 계산
    visited = [0] * (n+1)
    giga, wood_len = wood(r, 0)
    branch(giga, 0)
    print(wood_len, branch_len)
