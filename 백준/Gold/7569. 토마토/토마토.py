import sys
input = sys.stdin.readline
from collections import deque

if __name__ == '__main__': 
    m, n, h = map(int, input().split())
    tomato = []
    unripe = 0
    q = deque()
    for i in range(h):
        tmp = []
        for j in range(n):
            a = list(map(int, input().split()))
            tmp.append(a)
            unripe += a.count(0)
            for k in range(m): 
                if a[k] == 1:
                    q.append((i, j, k)) 
        tomato.append(tmp)

    #bfs
    today = 0
    dx = [0, 0, -1, 0, 1, 0]
    dy = [0, 0, 0, -1, 0, 1]
    dh = [-1, 1, 0, 0, 0, 0]

    while q and unripe:
        today += 1
        tmp_q = deque()
        for _ in range(len(q)):
            i, j, k = q.popleft()
            for d in range(6):
                ni, nj, nk = i+dh[d], j+dx[d], k+dy[d]
                if 0 <= ni < h and 0 <= nj < n and 0 <= nk < m:
                    if tomato[ni][nj][nk] == 0:
                        tomato[ni][nj][nk] = 1
                        unripe -= 1
                        tmp_q.append((ni, nj, nk))
        q = tmp_q

    print(-1) if unripe else print(today)