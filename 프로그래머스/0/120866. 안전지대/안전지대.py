def solution(board):
    n = len(board)
    safe = n * n
    direct = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                safe -= 1
                for k in range(8):
                    x, y = direct[k]
                    if 0 > i+x or i+x >= n or 0 > j+y or j+y >= n:
                        continue
                    if board[i+x][j+y] == 0:
                        board[i+x][j+y] = 2
                        safe -= 1       
    return safe