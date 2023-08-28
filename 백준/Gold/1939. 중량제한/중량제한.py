import sys
input = sys.stdin.readline
from collections import deque

if __name__ == '__main__':
    n, m = map(int, input().split())
    bridge = [[] for _ in range(n+1)]
    for _ in range(m):
        a, b, c = map(int, input().split())
        bridge[a].append((b,c))
        bridge[b].append((a,c))

    fac = list(map(int, input().split()))
    def bfs(now, w):
        q = deque()
        q.append(now)
        visited = [0] * (n+1) 
        visited[now] = 1 

        while q:
            now = q.popleft()
            for i, c in bridge[now]:
                if visited[i] == 0 and c >= w:
                    visited[i] = 1
                    q.append(i)
                else:
                    continue
        return True if visited[fac[1]] else False

    start, end = 0, 1e9
    result = 0

    while start <= end:
        mid = (start + end) // 2

        if bfs(fac[0], mid): 
            result = mid
            start = mid + 1
        else:
            end = mid - 1
    print(int(result))