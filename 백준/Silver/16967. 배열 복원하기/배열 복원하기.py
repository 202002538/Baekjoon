import sys
input = sys.stdin.readline

if __name__ == '__main__':
    h, w, x, y = map(int, input().split())
    B = []
    for _ in range(h+x):
        B.append(list(map(int, input().split())))
    
    #배열이 두번 겹친 구간 <- 겹친 값을 빼준다
    for i in range(h-x):
        for j in range(w-y):
            B[i + x][j + y] -= B[i][j]

    result = [] #결과 담기
    for i in range(h):
        result.append(B[i][:w])

    for r in result: #출력
        print(*r)