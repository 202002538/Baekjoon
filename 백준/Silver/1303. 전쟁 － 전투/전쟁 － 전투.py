import sys
input = sys.stdin.readline
from collections import deque

if __name__ == '__main__': 
    n, m = map(int, input().split())
    matrix = []
    for _ in range(m):
        matrix.append(list(input()[:-1]))

    visited = [[0] * n for _ in range(m)]
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    def bfs(x, y):
        q = deque()
        q.append((x, y))
        color = matrix[x][y]
        visited[x][y] = 1
        soldier = 1
        while q:
            x, y = q.popleft()
            for k in range(4):
                nx, ny = x + dx[k], y + dy[k]
                if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny] and matrix[nx][ny] == color:
                    visited[nx][ny] = 1
                    soldier += 1
                    q.append((nx, ny))
        return soldier, color

    result_B = 0
    result_W = 0
    for i in range(m):
        for j in range(n):
            if not visited[i][j]:
                num, col = bfs(i, j)
                if col == 'B':
                    result_B += num**2
                else:
                    result_W += num**2
    print(result_W, result_B)