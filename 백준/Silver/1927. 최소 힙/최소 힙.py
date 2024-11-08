import sys
input = sys.stdin.readline
import heapq

if __name__ == '__main__':
    n = int(input())
    hq = []
    for _ in range(n):
        x = int(input())
        if x == 0:
            if not hq:
                print(0)
            else:
                print(heapq.heappop(hq))
        else:
            heapq.heappush(hq, x)