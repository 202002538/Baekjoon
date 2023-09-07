import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

if __name__ == '__main__':
    n = int(input())
    count = 1
    while n:
        graph = []
        for _ in range(n):
            graph.append(list(map(int, input().split())))
        distance = [[INF] * n for _ in range(n)]

        dx = [-1, 0, 1, 0]
        dy = [0, -1, 0, 1]

        #시작점 세팅
        distance[0][0] = graph[0][0]
        hq = []
        heapq.heappush(hq, (graph[0][0], 0, 0)) #현재 개수, 좌표 순서

        while hq:
            dis, x, y = heapq.heappop(hq)
            if dis > distance[x][y]:
                continue
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < n and 0 <= ny < n:
                    cost = dis + graph[nx][ny]
                    if cost < distance[nx][ny]:
                        distance[nx][ny] = cost
                        heapq.heappush(hq, (cost, nx, ny))
        #출력
        print("Problem %d: %d" %(count, distance[n-1][n-1]))
        count += 1
        n = int(input())