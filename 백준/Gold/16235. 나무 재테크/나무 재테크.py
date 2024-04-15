import sys
input = sys.stdin.readline
from collections import deque

if __name__ == '__main__':
    n, m, k = map(int, input().split())
    ground = [[5] * (n+1) for _ in range(n+1)]  
    tree = [[deque() for _ in range(n+1)] for _ in range(n+1)] 
    nour = [[0] * (n+1)]
    for _ in range(n):
        nour.append([0] + list(map(int, input().split())))
    for _ in range(m):
        x, y, z = map(int, input().split())
        tree[x][y].append(z)

    dx = [-1, -1, -1, 0, 0, 1, 1, 1]
    dy = [-1, 0, 1, -1, 1, -1, 0, 1]

    while k > 0:
        breed = []
        for i in range(1, n+1):
            for j in range(1, n+1):
                tmp = deque()
                dead = 0
                while tree[i][j]: 
                    small = tree[i][j].popleft()
                    if ground[i][j] >= small: 
                        ground[i][j] -= small
                        tmp.append(small+1)
                        if (small+1) % 5 == 0: 
                            breed.append((i, j))
                    else:
                        dead += (small // 2)
                tree[i][j] = tmp.copy() 
                ground[i][j] += dead 
                ground[i][j] += nour[i][j] 

        while breed:
            i, j = breed.pop()
            for a in range(8):
                nx, ny = i + dx[a], j + dy[a]
                if 1 <= nx <= n and 1 <= ny <= n:
                    tree[nx][ny].appendleft(1)
        k -= 1

    result = 0
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if tree[i][j]:
                result += len(tree[i][j])
    print(result)