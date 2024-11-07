import sys
input = sys.stdin.readline
INF = 1e9
import heapq

if __name__ == '__main__':
    n, m = map(int, input().split())
    graph = [[] for _ in range(n+1)]
    for _ in range(m):
        a, b, c = map(int, input().split())
        graph[a].append((c, b))
        graph[b].append((c, a))

    hq = []
    heapq.heappush(hq, (0, 1))
    distance = [INF] * (n+1)
    distance[1] = 0
    while hq:
        dis, now = heapq.heappop(hq)
        if dis > distance[now]:
            continue
        for c, nxt in graph[now]:
            cost = dis + c
            if cost < distance[nxt]:
                distance[nxt] = cost
                heapq.heappush(hq, (cost, nxt))
    print(distance[n])