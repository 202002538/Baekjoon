from collections import deque
import sys
input = sys.stdin.readline

if __name__ == '__main__':
    n, m, k, x = map(int, input().split())
    road = [[] for _ in range(n+1)]

    for _ in range(m):
        s, d = map(int, input().split())
        road[s].append(d)

    distance = [-1] * (n+1)
    distance[x] = 0

    q = deque([x])
    while q:
        now = q.popleft()
        for c in road[now]:
            if distance[c] == -1:
                distance[c] = distance[now]+1
                q.append(c)

    if k not in distance:
        print(-1)
    else:
        for i in range(1, n+1):
            if distance[i] == k:
                print(i)