import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

if __name__ == '__main__':
    n, m, x = map(int, input().split())

    # 그래프 입력받기
    original_graph = [[] for _ in range(n + 1)]
    # 역방향으로도 저장: 모든 마을 -> 파티장소로 가는길 한번에 구함
    reverse_graph = [[] for _ in range(n + 1)]

    for _ in range(m):
        a, b, c = map(int, input().split())
        original_graph[a].append((b, c))
        reverse_graph[b].append((a, c))

    def dijkstra(start, graph):
        q = []
        distance = [INF] * (n + 1)

        # 시작노드에 대한 초기화
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

    #각 학생 x로 오는 시간
    distance = dijkstra(x, reverse_graph)

    #각 학생 가는 시간
    distance2 = dijkstra(x, original_graph)
    for i in range(1, n+1):
        distance[i] += distance2[i]

    print(max(distance[1:]))