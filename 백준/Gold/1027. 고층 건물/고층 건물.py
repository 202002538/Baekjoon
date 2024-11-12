import sys
input = sys.stdin.readline
INF = 1e9

if __name__ == '__main__':
    def left_view(a): #기울기 감소해야함
        see = 0
        slope = INF
        for j in range(a-1, -1, -1):
            new = (building[a] - building[j]) / (a - j)
            if new < slope:
                see += 1
                slope = new
        return see

    def right_view(a): #기울기 증가해야함
        see = 0
        slope = -INF
        for j in range(a+1, n):
            new = (building[j] - building[a]) / (j - a)
            if new > slope:
                see += 1
                slope = new
        return see

    n = int(input())
    building = list(map(int, input().split()))
    result = 0
    for i in range(n):
        result = max(result, left_view(i) + right_view(i))
    print(result)