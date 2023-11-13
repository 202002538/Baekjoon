import sys
input = sys.stdin.readline
from collections import deque

if __name__ == '__main__':
    n = int(input())
    crane = list(map(int, input().split()))
    m = int(input())
    box = list(map(int, input().split()))

    crane.sort(reverse=True)
    box.sort()

    able = True
    minute = 0
    box = deque(box)
    while able and box:
        minute += 1
        i, j = len(box)-1, 0
        #매 분마다, 크레인에 최대한 짐을 나눠준다
        while i >= 0 and j < len(crane):
            if box[i] <= crane[j]:
                box.remove(box[i])
                j += 1
            else:
                if i == len(box)-1 and j == 0: #옮길수없는 박스 존재
                    able = False
            i -= 1
    print(minute) if able else print(-1)