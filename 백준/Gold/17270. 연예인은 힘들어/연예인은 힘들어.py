INF = int(1e9)
import sys
import heapq
input = sys.stdin.readline

if __name__ == '__main__':
    n, m = map(int, input().split())

    # 그래프 입력받기(양방향 저장)
    graph = [[] for i in range(n + 1)]
    for _ in range(m):
        a, b, c = map(int, input().split())
        graph[a].append((b, c))
        graph[b].append((a, c))

    j, s = map(int, input().split())

    def dijkstra(start):
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

    jihun = dijkstra(j)
    sungha = dijkstra(s)

    candidate = []
    shortest = INF
    for i in range(1, n+1):
        if i != j and i != s:
            shortest = min(shortest, jihun[i]+sungha[i])
            if jihun[i] <= sungha[i]:
                #소요시간 합, 목적지 번호, 지헌시간, 성하시간 저장
                candidate.append((jihun[i]+sungha[i], i, jihun[i], sungha[i]))
    candidate.sort(key=lambda x: (x[0], x[2], x[1]))

    if len(candidate) == 0 or candidate[0][0] != shortest:
        print(-1)
    else:
        print(candidate[0][1])

