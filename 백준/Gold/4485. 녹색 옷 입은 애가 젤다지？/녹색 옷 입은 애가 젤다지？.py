import sys
input = sys.stdin.readline
INF = 1e9
import heapq

if __name__ == '__main__':
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    result = []
    while True:
        n = int(input())
        if not n:
            break

        cave = []
        loss = [[INF] * n for _ in range(n)]
        for _ in range(n):
            cave.append(list(map(int, input().split())))

        loss[0][0] = cave[0][0]
        hq = []
        heapq.heappush(hq, (cave[0][0], 0, 0))
        while hq:
            dis, x, y = heapq.heappop(hq)
            if dis > loss[x][y]:
                continue
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if nx < 0 or nx >= n or ny < 0 or ny >= n:
                    continue
                cost = loss[x][y] + cave[nx][ny]
                if loss[nx][ny] > cost:
                    loss[nx][ny] = cost
                    heapq.heappush(hq, (cost, nx, ny))
        result.append(loss[n-1][n-1])

    for i, r in enumerate(result):
        print(f'Problem {i+1}: {r}')