import sys
input = sys.stdin.readline
INF = 1e9
import heapq

if __name__ == '__main__':
    n, m = map(int, input().split())
    board = []
    for i in range(n):
        tmp = list(map(int, input().split()))
        board.append(tmp)
        if 2 in tmp:
            a, b = i, tmp.index(2)

    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    distance = [[INF] * m for _ in range(n)]
    hq = []
    heapq.heappush(hq, (0, a, b))
    distance[a][b] = 0

    while hq:
        dis, x, y = heapq.heappop(hq)
        if dis > distance[x][y]:
            continue
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and board[nx][ny] == 1:
                cost = dis + 1
                if cost < distance[nx][ny]:
                    distance[nx][ny] = cost
                    heapq.heappush(hq, (cost, nx, ny))

    for i in range(n):
        for j in range(m):
            if board[i][j] == 0:
                print('0', end=' ')
            elif distance[i][j] == INF:
                print('-1', end=' ')
            else:
                print(distance[i][j], end=' ')
        print()