import sys
input = sys.stdin.readline
from collections import deque

if __name__ == '__main__':
    n, l, r = map(int, input().split())
    nation = []
    for _ in range(n):
        nation.append(list(map(int, input().split())))

    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    def bfs(x, y, checked):
        alliance = [(x, y)]
        q = deque([(x, y)])
        people = nation[x][y]
        checked[x][y] = 1
        while q:
            x, y = q.popleft()
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if 0 <= nx < n and 0 <= ny < n and not checked[nx][ny]:
                    if l <= abs(nation[x][y] - nation[nx][ny]) <= r:
                        people += nation[nx][ny]
                        checked[nx][ny] = 1
                        q.append((nx, ny))
                        alliance.append((nx, ny))
        if len(alliance) > 1:
            tmp = people // len(alliance)
            for x, y in alliance:
                nation[x][y] = tmp
            return True
        else:
            return False

    day = 0
    while True:
        move = 0
        checked = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if not checked[i][j]:
                    if bfs(i, j, checked):
                        move = 1
        if move:
            day += 1
        else:
            print(day)
            break