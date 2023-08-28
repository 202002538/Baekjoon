import sys
input = sys.stdin.readline
from heapq import heapify, heappop, heappush

if __name__ == '__main__':
    n = int(input())
    cards = [int(input()) for _ in range(n)]
    heapify(cards)

    #그리디 -> 가장 작은 묶음 2개 꺼내 합침
    result = 0
    while len(cards) >= 2:
        a = heappop(cards)
        b = heappop(cards)

        result += (a + b)
        heappush(cards, a+b)

    print(result)