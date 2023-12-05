import sys
input = sys.stdin.readline

if __name__ == '__main__':
    n = int(input())
    dot = [[] for _ in range(n+1)]
    for _ in range(n):
        x, y = map(int, input().split())
        dot[y].append(x)

    result = 0
    for i in range(1, n+1):
        if len(dot[i]) > 1: #그 색깔 점이 2개 이상
            dot[i].sort()
            result += dot[i][1] - dot[i][0]
            result += dot[i][-1] - dot[i][-2]
            
            for j in range(1, len(dot[i])-1):
                nearest = min(dot[i][j] - dot[i][j-1],
                              dot[i][j+1] - dot[i][j])
                result += nearest
    print(result)