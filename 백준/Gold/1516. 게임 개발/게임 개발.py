import sys
input = sys.stdin.readline
from collections import deque

if __name__ == '__main__':
    n = int(input())
    indgree = [0] * (n+1) 
    time = [0] * (n+1)
    next = [[] for _ in range(n+1)]

    for i in range(1, n+1):
        tmp = list(map(int, input().split()))
        time[i] = tmp[0]
        indgree[i] = len(tmp) - 2
        for t in tmp[1: -1]:
            next[t].append(i)

    #위상정렬
    q = deque()
    least_time = time.copy()

    for i in range(1, n+1):
        if indgree[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()
        for ne in next[now]:
            least_time[ne] = max(least_time[ne], time[ne]+least_time[now])
            indgree[ne] -= 1
            if indgree[ne] == 0:
                q.append(ne)

    for l in least_time[1:]:
        print(l)