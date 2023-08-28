import sys
input = sys.stdin.readline

if __name__ == '__main__':
    n = int(input())
    hall = [] 
    temp = [[0]*n for _ in range(n)]
    for _ in range(n):
        hall.append(list(input().split()))

    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    result = False
    teacher = []
   
    for i in range(n):
        for j in range(n):
            if hall[i][j] == 'T':
                teacher.append((i, j))

    def watch(x, y, dx, dy):
        nx = x + dx
        ny = y + dy
        if 0 <= nx < n and 0 <= ny < n:
            if temp[nx][ny] == 'S':
                return 1
            if temp[nx][ny] == 'X':
                return 0 + watch(nx, ny, dx, dy)
        return 0

    def dfs(count):
        global result
        if count == 3:
            for i in range(n):
                for j in range(n):
                    temp[i][j] = hall[i][j]
            total = 0
            for x, y in teacher:
                for i in range(4):
                    total += watch(x, y, dx[i], dy[i])
            if total == 0:
                result = True
            return
        for i in range(n):
            for j in range(n):
                if hall[i][j] == 'X': 
                    hall[i][j] = 'O'
                    count += 1
                    dfs(count)
                    hall[i][j] = 'X'
                    count -= 1

    dfs(0)
    print("YES" if result else "NO")