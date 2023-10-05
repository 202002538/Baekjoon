import sys
input = sys.stdin.readline
from collections import deque
import copy

if __name__ == '__main__':
    n, m = map(int, input().split())
    x, y, d = map(int, input().split())
    dir = [0, 1, 2, 3] #북, 동, 남, 서

    dx = [-1, 0, 1, 0] #북, 동, 남, 서
    dy = [0, 1, 0, -1]

    room = []
    for _ in range(n):
        room.append(list(map(int, input().split())))
    clean = copy.deepcopy(room)

    #시작지점은 현재 좌표
    q = deque()
    q.append((x, y))
    result = 0

    while q:
        x, y = q.popleft()

        #현재칸이 청소되지 않은 경우 청소
        if not clean[x][y]:
            result += 1
            clean[x][y] = 1

        uncleaned = 0 #주변 4칸 -> 청소되지 않은 빈칸 존재여부 확인
        for i in range(4):
            if room[x+dx[i]][y+dy[i]] == 0 and not clean[x+dx[i]][y+dy[i]]:
                uncleaned += 1

        if uncleaned:
            move = 1
            while move: #한칸 전진할 때까지
                d -= 1 #반시계 회전
                if d == -1:
                    d = 3
                #바라보는 칸이 청소되지 않은 빈칸인 경우 전진
                if room[x+dx[d]][y+dy[d]] == 0 and not clean[x+dx[d]][y+dy[d]]:
                    q.append((x+dx[d], y+dy[d]))
                    move = 0
        else:
            if d == 0 or d == 1: #후진
                backdir = d + 2
            else:
                backdir = d - 2
            #가능하면 그 위치로 이동
            if room[x+dx[backdir]][y+dy[backdir]] == 0:
                q.append((x+dx[backdir], y+dy[backdir]))

    print(result)
