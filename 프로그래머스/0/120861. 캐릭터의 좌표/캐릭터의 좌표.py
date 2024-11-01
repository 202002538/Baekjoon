def solution(keyinput, board):
    answer = []
    width = [-(board[0]-1) / 2, (board[0]-1) / 2]
    depth = [-(board[1]-1) / 2, (board[1]-1) / 2]

    x, y = 0, 0
    key = {'left': (-1, 0), 'right': (1, 0), 'up': (0, 1), 'down': (0, -1)}
    for ky in keyinput:
        a, b = key[ky]
        nx, ny = x + a, y + b
        if width[0] > nx or width[1] < nx or depth[0] > ny or depth[1] < ny:
            continue
        x, y = nx, ny
    
    return [x, y]