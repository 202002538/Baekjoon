import sys
input = sys.stdin.readline
import heapq

if __name__ == '__main__':
    n, m = map(int, input().split())
    corn = []
    hq = []
    for i in range(n):
        tmp = list(map(int, input().split()))
        corn.append(tmp)
    k = int(input())

    visited = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if i == 0 or i == n-1 or j == 0 or j == m-1:
                heapq.heappush(hq, (-corn[i][j], i, j))

    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]

    result = []
    while hq and k != 0:
        v, x, y = heapq.heappop(hq)

        if not visited[x][y]:
            visited[x][y] = 1
            result.append((x, y)) 
            k -= 1
            #방문가능한 주변 좌표
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                    heapq.heappush(hq, (-corn[nx][ny], nx, ny))

    for x, y in result:
        print(x+1, y+1)