import sys
input = sys.stdin.readline

if __name__ == '__main__':

    n, m = map(int, input().split())
    lab = []
    temp = [[0] * m for _ in range(n)]
    for _ in range(n):
        lab.append(list(map(int, input().split())))
        
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    result = 0

    def virus(x, y):
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if temp[nx][ny] == 0: 
                temp[nx][ny] = 2
                virus(nx, ny)

    def get_score():
        safe = 0
        for i in range(n):
            for j in range(m):
                if temp[i][j] == 0:
                    safe += 1
        return safe

    def dfs(start, count):
        global result
        if count == 3:
            for i in range(n):
                for j in range(m):
                    temp[i][j] = lab[i][j] 
            for i in range(n):
                for j in range(m):
                    if temp[i][j] == 2:
                        virus(i, j)
            result = max(result, get_score())
            return
        for i in range(start, n * m):
            x = (int)(i / m)
            y = (int)(i % m)

            if lab[x][y] == 0:
                lab[x][y] = 1
                dfs(i + 1, count + 1)
                lab[x][y] = 0

    dfs(0, 0)
    print(result)