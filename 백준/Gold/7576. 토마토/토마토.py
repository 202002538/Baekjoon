import sys
input = sys.stdin.readline
from collections import deque

if __name__ == '__main__': #백준 25195
    n, m = map(int, input().split())
    box = []
    for _ in range(m):
        box.append(list(map(int, input().split())))

    #익은 토마토 위치 큐에 담기
    q = deque()
    for i in range(m):
        for j in range(n):
            if box[i][j] == 1:
                q.append((i, j, 0))

    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]

    #bfs
    max_day = 0
    while q:
        x, y, day = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < m and 0 <= ny < n:
                if box[nx][ny] == 0: #주위 안익은것 -> 익히고 큐에 위치담기
                    box[nx][ny] = 1
                    q.append((nx, ny, day+1))
        max_day = day

    #bfs이후 안익은 토마토 여부
    raw = 0
    for i in range(m):
        for j in range(n):
            if box[i][j] == 0:
                raw = 1
                break
    print(-1) if raw else print(max_day)