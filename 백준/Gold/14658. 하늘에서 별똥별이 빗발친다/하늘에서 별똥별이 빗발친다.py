import sys
input = sys.stdin.readline

if __name__ == '__main__':
    n, m, l, k = map(int, input().split())
    star = []
    for _ in range(k):
        x, y = map(int, input().split())
        star.append((x, y))

    result = 0
    for i in range(k):
        for j in range(k):
            #첫번째 별의 x좌표와 두번째 별의 y좌표가 기준이 됨
            x = star[i][0]
            y = star[j][1]
            count = 0
            for a in range(k):
                if x <= star[a][0] <= x+l and y <= star[a][1] <= y+l:
                    count += 1
            result = max(result, count)
    print(k - result)