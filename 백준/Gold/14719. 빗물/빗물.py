import sys
input = sys.stdin.readline

h, w = map(int, input().split())
block = list(map(int, input().split()))

world = [[0] * w for _ in range(h)]
for i, n in enumerate(block):
    for j in range(n):
        world[j][i] = 1

result = 0
for i in range(h):
    for j in range(w):
        if world[i][j] == 1:
            if 1 in world[i][j+1:]:
                nxt = world[i].index(1, j+1, w)
                result += nxt-j-1
print(result)