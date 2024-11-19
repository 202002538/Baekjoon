import sys
input = sys.stdin.readline
from collections import deque
INF = 1e9
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(input()[:-1]))

distance = [[INF] * m for _ in range(n)]
visited = [[[0] * 2 for _ in range(m)] for _ in range(n)]
#visited[x][y][0] - 블록을 부수지 않고 진행한 경로/ [x][y][1] - 블록을 부수고 진행

def bfs(x, y, z):
    q = deque([(x, y, z)]) 
    visited[x][y][z] = 1
    while q:
        x, y, smash = q.popleft()
        if x == n-1 and y == m-1:
            return visited[x][y][smash]
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                #벽이고, 더 부술 수 있음
                if graph[nx][ny] == '1' and smash == 0:
                    visited[nx][ny][1] = visited[x][y][0] + 1
                    q.append((nx, ny, 1))
                #벽이 아님
                elif graph[nx][ny] == '0' and not visited[nx][ny][smash]:
                    visited[nx][ny][smash] = visited[x][y][smash] + 1
                    q.append((nx, ny, smash))
    return -1
print(bfs(0, 0, 0))