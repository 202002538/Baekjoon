import sys
input = sys.stdin.readline

if __name__ == '__main__':
    n, m, r = map(int, input().split())
    direction = {'E': 1, 'W': -1, 'S': 1, 'N': -1}
    game = []
    for _ in range(n):
        game.append(list(map(int, input().split())))
    domino = [['S'] * m for _ in range(n)]

    result = 0
    for _ in range(r):
        #공격
        x, y, d = input().split()
        x = int(x) - 1
        y = int(y) - 1

        dx, dy = 0, 0 
        if d == 'E' or d == 'W':
            dy = direction[d]
        else:
            dx = direction[d]

        fall = 1
        while 0 <= x < n and 0 <= y < m and fall >= 1:
            if domino[x][y] == 'S': 
                domino[x][y] = 'F'
                result += 1
                fall = max(fall, game[x][y])

            fall -= 1
            x += dx
            y += dy

        #수비
        x, y = map(int, input().split())
        domino[x-1][y-1] = 'S'

    print(result)
    for a in range(n):
        for b in range(m):
            print(domino[a][b], end=" ")
        print()