import sys
input = sys.stdin.readline
INF = 1e9
import heapq

if __name__ == '__main__':
    n, m, x = map(int, input().split())
    original = [[] for _ in range(n+1)]
    reverse = [[] for _ in range(n+1)]

    for _ in range(m):
        a, b, t = map(int, input().split())
        original[a].append((b, t))
        reverse[b].append((a,t))

    def dijkstra(graph, x):
        distance = [INF] * (n+1)
        distance[x] = 0
        hq = []
        heapq.heappush(hq, (0, x))
        while hq:
            dis, now = heapq.heappop(hq)
            if dis > distance[now]:
                continue
            for g, time in graph[now]:
                cost = dis + time
                if cost < distance[g]:
                    distance[g] = cost
                    heapq.heappush(hq, (cost, g))
        return distance

    # 각자 마을 -> 파티장으로의 다익스트라(파티장에서의 역순으로)
    go = dijkstra(reverse, x)
    # 파티장 -> 각자 마을로의 다익스트라
    back = dijkstra(original, x)

    result = 0
    for i in range(1, n+1):
        result = max(result, go[i]+back[i])
    print(result)