import sys
input = sys.stdin.readline
from queue import PriorityQueue

if __name__ == '__main__':
    n = int(input())
    q = PriorityQueue()
    for _ in range(n):
        q.put(int(input()))

    #greedy
    result = 0
    while q.qsize() >= 2:
        a = q.get()
        b = q.get()

        result += (a + b)
        q.put(a + b)

    print(result)