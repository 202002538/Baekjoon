import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

if __name__ == '__main__':
    n = int(input())
    m = int(input())
    graph = [[] for _ in range(n+1)]
    for _ in range(m):
        a, b, c = map(int, input().split())
        graph[a].append((b, c))
    start, end = map(int, input().split())

    #최단거리 저장 테이블
    distance = [INF] * (n+1)

    #시작점 세팅
    distance[start] = 0
    hq = []
    heapq.heappush(hq, (0, start))

    #다익스트라
    while hq:
        dis, now = heapq.heappop(hq)
        if dis > distance[now]:
            continue
        for i in graph[now]:
            temp = dis + i[1]
            if temp < distance[i[0]]:
                distance[i[0]] = temp
                heapq.heappush(hq, (temp, i[0]))
    print(distance[end])