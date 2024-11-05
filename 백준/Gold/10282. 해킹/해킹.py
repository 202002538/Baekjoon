import sys
input = sys.stdin.readline
INF = 1e9
import heapq

if __name__ == '__main__':
    result = []
    for _ in range(int(input())):
        n, d, c = map(int, input().split())
        graph = [[] for _ in range(n+1)]
        for _ in range(d):
            a, b, s = map(int, input().split())
            graph[b].append((a, s))

        reach = [INF] * (n+1)

        q = []
        heapq.heappush(q, (0, c)) 
        reach[c] = 0
        while q:
            dis, now = heapq.heappop(q)
            if dis > reach[now]:
                continue
            for sub, time in graph[now]:
                if dis + time < reach[sub]:
                    reach[sub] = dis + time
                    heapq.heappush(q, (reach[sub], sub))

        infected, time = 0, 0
        for r in reach:
            if r == INF:
                continue
            infected += 1
            time = max(time, r)
        result.append([infected, time])

    for k in result:
        print(*k)