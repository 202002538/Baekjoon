import sys
input = sys.stdin.readline

def solution(board, skill):
    answer = 0
    d, w = len(board), len(board[0])
    apply = [[0] * (w+1) for _ in range(d+1)]

    for s in skill:
        type_, r1, c1, r2, c2, degree = s[0], s[1], s[2], s[3], s[4], s[5]
        change = degree * (-1)**type_
        apply[r1][c1] += change
        apply[r1][c2+1] += change * (-1)
        apply[r2+1][c2+1] += change
        apply[r2+1][c1] += change * (-1)

    for i in range(d):
        for j in range(1, w):
            apply[i][j] += apply[i][j-1]

    for i in range(w):
        for j in range(1, d):
            apply[j][i] += apply[j-1][i]

    #최종
    for i in range(d):
        for j in range(w):
            if board[i][j] + apply[i][j] > 0:
                answer += 1
    return answer