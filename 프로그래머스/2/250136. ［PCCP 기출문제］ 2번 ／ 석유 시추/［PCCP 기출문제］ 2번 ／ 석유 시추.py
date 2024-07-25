import sys
input = sys.stdin.readline
from collections import deque

dx = [0,0,-1,1]
dy = [1,-1,0,0]

def bfs(a, b, num, land):
    q = deque()
    oil = 1
    q.append((a, b))
    land[a][b] = num
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= len(land) or ny >= len(land[0]):
                continue
            if land[nx][ny] == 1:
                q.append((nx, ny))
                land[nx][ny] = num
                oil += 1
    return oil, land

def solution(land):
    total_oil = {0: 0}
    num = 2
    for i in range(len(land)):
        for j in range(len(land[0])):
            if land[i][j] == 1:
                oil, land = bfs(i, j, num, land)
                total_oil[num] = oil
                num += 1

    max_oil = 0
    for i in range(len(land[0])):
        nums = list(map(lambda j: land[j][i], range(0, len(land))))
        oil_get = sum(map(lambda x: total_oil[x], set(nums)))
        max_oil = max(max_oil, oil_get)

    return max_oil