import sys
input = sys.stdin.readline

if __name__ == '__main__':
    n, m = map(int, input().split())
    k = int(input())
    matrix = []
    for _ in range(n):
        matrix.append(list(input())[:-1])

    #누적합
    sum_j = [[0] * (m+1) for _ in range(n+1)]
    sum_i = [[0] * (m+1) for _ in range(n+1)]
    sum_o = [[0] * (m+1) for _ in range(n+1)]
    for i in range(1, n+1):
        for j in range(1, m+1):
            if matrix[i-1][j-1] == 'J':
                sum_j[i][j] += 1
            elif matrix[i-1][j-1] == 'I':
                sum_i[i][j] += 1
            else:
                sum_o[i][j] += 1
            sum_j[i][j] = sum_j[i - 1][j] + sum_j[i][j - 1] - sum_j[i - 1][j - 1] + sum_j[i][j]
            sum_i[i][j] = sum_i[i - 1][j] + sum_i[i][j - 1] - sum_i[i - 1][j - 1] + sum_i[i][j]
            sum_o[i][j] = sum_o[i - 1][j] + sum_o[i][j - 1] - sum_o[i - 1][j - 1] + sum_o[i][j]

    #원하는 영역 정보 출력
    for _ in range(k):
        a, b, c, d = map(int, input().split())
        result_j = sum_j[c][d] - sum_j[c][b-1] - sum_j[a-1][d] + sum_j[a-1][b-1]
        result_i = sum_i[c][d] - sum_i[c][b - 1] - sum_i[a - 1][d] + sum_i[a - 1][b - 1]
        result_o = sum_o[c][d] - sum_o[c][b - 1] - sum_o[a - 1][d] + sum_o[a - 1][b - 1]
        print(result_j, result_o, result_i)