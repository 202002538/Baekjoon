import sys
input = sys.stdin.readline

if __name__ == '__main__':
    r, c = map(int, input().split())
    bread = []
    for _ in range(r):
        bread.append(list(input())[:-1])

    dx = [-1, 0, 1]
    dy = [1, 1, 1]
    count = 0
    def dfs(x, y):
        global count
        if y == c-1:
            count += 1
            return True

        for i in range(3):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < r and 0 <= ny < c and bread[nx][ny] == '.':
                bread[nx][ny] = 'x'
                if dfs(nx, ny): 
                    return True
        return False

    for row in range(r):
        dfs(row, 0)

    print(count)
