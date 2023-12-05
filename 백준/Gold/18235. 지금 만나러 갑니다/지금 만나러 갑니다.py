import sys
input = sys.stdin.readline
from collections import deque

if __name__ == '__main__':
    n, duck1, duck2 = map(int, input().split())

    def bfs(q):
        while q:
            today, now = q.popleft()
            jump = 2**(today-1)
            if not now[0] or not now[1]:
                return -1

            #각 오리별 현재위치 -> 오늘 갈 수 있는 번호 파악
            for i in range(2):
                tmp = []
                for j in now[i]:
                    if j - jump > 0:
                        tmp.append(j - jump)
                    if j + jump <= n:
                        tmp.append(j + jump)
                now[i] = tmp.copy()

            #공통원소 확인
            common = set(now[0]).intersection(now[1])
            if len(common) > 0:
                return today

            q.append((today+1, now))
        return -1

    q = deque()
    q.append((1, [[duck1], [duck2]]))
    result = bfs(q)
    print(result)