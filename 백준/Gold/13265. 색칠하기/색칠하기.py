import sys
input = sys.stdin.readline

if __name__ == '__main__':
    t = int(input())
    answer = []
    for _ in range(t):
        n, m = map(int, input().split())
        edge = [[] for _ in range(n+1)]
        for _ in range(m):
            a, b = map(int, input().split())
            edge[a].append(b)
            edge[b].append(a)

        color = [0] * (n+1)

        result = True
        def dfs(now, paint):
            global result
            if paint == 1:
                paint = 2
            else:
                paint = 1

            for e in edge[now]:
                if color[e] == color[now]:
                    result = False
                elif color[e] == 0:
                    color[e] = paint
                    dfs(e, paint)

        while 0 in color[1:]:
            idx = color.index(0, 1, len(color))
            color[idx] = 1
            dfs(idx, 1)

        answer.append("possible" if result else "impossible")

    for a in answer:
        print(a)