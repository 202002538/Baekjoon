from collections import deque
import sys
input = sys.stdin.readline
import copy

if __name__ == '__main__':
    n, k = map(int, input().split())
    exp = []
    for _ in range(n):
        exp.append(list(map(int, input().split())))
    s, tx, ty = map(int, input().split())
    virus = []

    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    for i in range(n):
        for j in range(n):
            if exp[i][j] != 0:
                virus.append((exp[i][j], 0, i, j))

    virus.sort()
    q = deque(virus)

    while q:
        num, time, x, y = q.popleft()
        if time == s:
            break
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if exp[nx][ny] == 0:
                    exp[nx][ny] = num
                    q.append((num, time+1, nx, ny))

    print(exp[tx-1][ty-1])