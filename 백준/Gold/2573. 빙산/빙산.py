import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())
ice = []
for _ in range(n):
    ice.append(list(map(int, input().split())))

#동서남북 맞닿은 바다 개수 체크
near = [[0] * m for _ in range(n)]
for i in range(n):
    for j in range(m):
        if ice[i][j] == 0: #이미 바다인곳은 신경안씀
            continue

        count = 0
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nx, ny = i + dx, j + dy
            if 0 <= nx < n and 0 <= ny < m and ice[nx][ny] == 0:
                count += 1
        near[i][j] = count

# 빙산 덩어리 개수세기
def count_ice(ice):
    tmp = [[0] * m for _ in range(n)]

    def dfs(x, y):
        q = deque()
        q.append((x, y))
        while q:
            x, y = q.popleft()
            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < m and ice[nx][ny] != 0 and tmp[nx][ny] == 0:
                    q.append((nx, ny))
                    tmp[nx][ny] = 1

    count = 0
    for i in range(n):
        for j in range(m):
            if ice[i][j] != 0 and tmp[i][j] == 0: #새 빙하 발견
                dfs(i, j)
                count += 1
    return count

def melt(ice):
    q = deque()
    for i in range(n):
        for j in range(m):
            if ice[i][j] == 0:
                continue
            ice[i][j] -= near[i][j]
            #빙산 높이가 0이 된것들 -> 근처 빙하의 near이 증가
            #모아왔다가 따로 처리. 이번 턴에 영향없도록
            if ice[i][j] <= 0:
                ice[i][j] = 0
                q.append((i, j))

    while q:
        i, j = q.popleft()
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nx, ny = i + dx, j + dy
            if 0 <= nx < n and 0 <= ny < m and ice[nx][ny] != 0:
                near[nx][ny] += 1

result = 0
while True: # 두덩어리 이상까지 반복
    ices = count_ice(ice)
    if ices >= 2:
        print(result)
        break
    if ices == 0:
        print(0)
        break
    melt(ice)
    result += 1