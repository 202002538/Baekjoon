import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

if __name__ == '__main__':
    def find(parent, x):
        if x != parent[x]:
            parent[x] = find(parent, parent[x])
        return parent[x]

    def union(parent, a, b):
        a = find(parent, a)
        b = find(parent, b)
        if a > b:
            parent[a] = b
        else:
            parent[b] = a

    #input
    n, m = map(int, input().split())
    map = []
    for _ in range(n):
        map.append([i for i in input()][:-1])

    direct = ['U', 'D', 'L', 'R']
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    #모든 좌표에 대해 합집합 연산해주기
    parent = [i for i in range(n*m)]
    for x in range(n):
        for y in range(m):
            # 이동한 방향의 좌표 확인
            now = map[x][y]
            nx = x + dx[direct.index(now)]
            ny = y + dy[direct.index(now)]

            #올바른 좌표면 현재좌표 - 이동한 좌표 합집합
            # x * m + y로 2차원 좌표 -> 1차원 좌표 할당
            if 0 <= nx < n and 0 <= ny < m:
                num_now = x * m + y
                num_move = nx * m + ny
                union(parent, num_now, num_move)

    #모든 좌표에 대해 find(경로압축)
    #parent = root가 되도록
    for a in range(n*m):
        p = find(parent, a)

    print(len(set(parent)))