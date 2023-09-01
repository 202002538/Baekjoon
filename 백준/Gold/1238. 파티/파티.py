import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

if __name__ == '__main__':
    n, m, x = map(int, input().split())

    # 그래프 입력받기
    graph = [[] for i in range(n + 1)]
    for _ in range(m):
        a, b, c = map(int, input().split())
        graph[a].append((b, c))

    def dijkstra(start):
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

    time = [0] * (n+1)
    #각 학생 오는 시간 저장
    for i in range(1, n+1):
        distance = dijkstra(i)
        time[i] += distance[x]

    #각 학생 가는 시간 저장
    distance = dijkstra(x)
    for i in range(1, n+1):
        time[i] += distance[i]

    print(max(time))