import sys
input = sys.stdin.readline

def solution(rows, columns, queries):
    answer = []
    matrix = [[0] * (columns+1) for _ in range(rows+1)]
    for i in range(rows+1):
        for j in range(columns+1):
            matrix[i][j] = (i-1) * columns + j

    result = []
    for x1, y1, x2, y2 in queries:
        tmp1 = matrix[x1][y1]
        num = tmp1
        for i in range(y1, y2):
            tmp2 = matrix[x1][i+1]
            matrix[x1][i+1] = tmp1
            tmp1 = tmp2
            num = min(num, tmp1)
        for i in range(x1, x2):
            tmp2 = matrix[i+1][y2]
            matrix[i+1][y2] = tmp1
            tmp1 = tmp2
            num = min(num, tmp1)
        for i in range(y2, y1, -1):
            tmp2 = matrix[x2][i-1]
            matrix[x2][i-1] = tmp1
            tmp1 = tmp2
            num = min(num, tmp1)
        for i in range(x2, x1, -1):
            tmp2 = matrix[i-1][y1]
            matrix[i-1][y1] = tmp1
            tmp1 = tmp2
            num = min(num, tmp1)
        result.append(num)

    return result