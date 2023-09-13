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
    def bfs(now, w): #너비 우선 탐색으로 중량 w를 들고 도달할 수 있는 모든 섬 확인
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
        return visited[fac[1]] #1번 공장 도달여부 반환 

    start, end = 0, 1e9
    result = 0

    while start <= end: #이분탐색으로 들고 건널 중량을 정함
        mid = (start + end) // 2

        if bfs(fac[0], mid): #0번 공장에서 해당 중량을 들고 출발, 1번 공장에 도달할 수 있나?
            result = mid
            start = mid + 1
        else:
            end = mid - 1
    print(int(result))