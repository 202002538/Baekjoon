INF = int(1e9)
import sys
input = sys.stdin.readline
from collections import deque

if __name__ == '__main__':
    r1, c1 = map(int, input().split())
    r2, c2 = map(int, input().split())
    n, m = 9, 10
    visited = [[INF] * n for _ in range(m)]

    dx = [-3, -2, -3, -2, 2, 3, 2, 3]
    dy = [-2, -3, 2, 3, -3, -2, 3, 2]
    king = [[(-1, 0), (-2, -1)], [(0, -1), (-1, -2)], [(-1, 0), (-2, 1)], [(0, 1), (-1, 2)],
            [(0, -1), (1, -2)], [(1, 0), (2, -1)], [(0, 1), (1, 2)], [(1, 0), (2, 1)]]

    def bfs(x, y):
        q = deque()
        q.append((x, y))
        visited[x][y] = 0

        while q:
            x, y = q.popleft()
            for i in range(8):
                nx, ny = x + dx[i], y + dy[i]
                if (0 <= nx < m and 0 <= ny < n) and visited[nx][ny] == INF and \
                        not (r2 == x + king[i][0][0] and c2 == y + king[i][0][1]) and \
                        not (r2 == x + king[i][1][0] and c2 == y + king[i][1][1]):
                    visited[nx][ny] = visited[x][y] + 1
                    if nx == r2 and ny == c2:
                        return visited[nx][ny]
                    q.append((nx, ny))
        return -1

    print(bfs(r1, c1))