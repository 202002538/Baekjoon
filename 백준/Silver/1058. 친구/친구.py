INF = int(1e9)
import sys
input = sys.stdin.readline

if __name__ == '__main__':
    n = int(input())

    #플로이드 표 초기화
    floyd = [([INF] * n) for _ in range(n)]
    for i in range(n):
        floyd[i][i] = 0
    for i in range(n):
        friend = input()
        for j, f in enumerate(friend):
            if f == 'Y':
                floyd[i][j] = 1

    #플로이드 워셜
    for i in range(n):
        for j in range(n):
            for k in range(n):
                floyd[i][j] = min(floyd[i][j], floyd[i][k] + floyd[k][j])

    #2-친구수 카운트
    result = 0
    for i in range(n):
        count = 0
        for j in floyd[i]:
            if 0 < j <= 2:
                count += 1
        result = max(result, count)
    print(result)