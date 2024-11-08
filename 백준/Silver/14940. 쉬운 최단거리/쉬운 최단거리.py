import sys
input = sys.stdin.readline
from collections import deque

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
    visited = [[0] * m for _ in range(n)]

    q = deque()
    q.append((a, b))
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and \
                    visited[nx][ny] == 0 and board[nx][ny] == 1:
                visited[nx][ny] = visited[x][y] + 1
                q.append((nx, ny))

    for i in range(n):
        for j in range(m):
            if visited[i][j] == 0 and board[i][j] == 1:
                print(-1, end=' ')
            else:
                print(visited[i][j], end=' ')
        print()