INF= 1e9
import sys
input = sys.stdin.readline
import heapq

def solution(n, s, a, b, fares):
    graph = [[] for _ in range(n+1)]

    for i, j, d in fares:
        graph[i].append((j, d))
        graph[j].append((i, d))

    def dijkstra(start):
        visited = [False] * (n + 1)
        distance = [INF] * (n + 1)
        q = []

        heapq.heappush(q, (0, start))
        distance[start] = 0

        while q:
            dist, now = heapq.heappop(q)
            if distance[now] < dist:
                continue
            for i in graph[now]:
                cost = dist + i[1]
                if cost < distance[i[0]]:
                    distance[i[0]] = cost
                    heapq.heappush(q, (cost, i[0]))
        return distance

    dis_s = dijkstra(s)
    dis_a = dijkstra(a)
    dis_b = dijkstra(b)
    result = INF
    
    for i in range(1, n+1): # i: 헤어지는 지점
        tmp = dis_s[i] + dis_a[i] + dis_b[i]
        result = min(result, tmp)
    return result