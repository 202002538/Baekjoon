import sys
input = sys.stdin.readline
import heapq

if __name__ == '__main__':
    n, m = map(int, input().split())
    indegree = [0] * (n+1)
    graph = [[] for _ in range(n+1)]
    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        indegree[b] += 1

    hq = []
    for i in range(1, n+1):
        if indegree[i] == 0:
            heapq.heappush(hq, i)

    result = []
    while hq:
        i = heapq.heappop(hq)
        result.append(i)
        for g in graph[i]:
            indegree[g] -= 1
            if indegree[g] == 0:
                heapq.heappush(hq, g)

    print(*result)