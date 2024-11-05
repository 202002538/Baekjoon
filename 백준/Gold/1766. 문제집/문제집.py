import sys
input = sys.stdin.readline
import heapq

if __name__ == '__main__':
    n, m = map(int, input().split())
    prob = [[] for _ in range(n+1)]
    indegree = [0] * (n+1)
    for _ in range(m):
        a, b = map(int, input().split())
        indegree[b] += 1
        prob[a].append(b)

    hq = []
    for i in range(1, n+1):
        if indegree[i] == 0:
            heapq.heappush(hq, i)

    result = []
    while hq:
        now = heapq.heappop(hq)
        result.append(now)
        for p in prob[now]:
            indegree[p] -= 1
            if indegree[p] == 0:
                heapq.heappush(hq, p)

    print(*result)