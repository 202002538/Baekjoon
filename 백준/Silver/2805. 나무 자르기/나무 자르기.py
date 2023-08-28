import sys
input = sys.stdin.readline
from collections import Counter
if __name__ == '__main__':
    n, m = map(int, input().split())
    tteok = Counter(map(int, input().split()))

    start = 0
    end = max(tteok)

    #이진탐색 수행
    result = 0
    while start <= end:
        mid = (start + end) // 2
        total = sum((h - mid) * i for h, i in tteok.items() if h > mid)

        if total < m:
            end = mid - 1
        else:
            result = mid
            start = mid + 1

    print(result)