import sys
input = sys.stdin.readline

if __name__ == '__main__':
    n, m = map(int, input().split())
    title = []
    for _ in range(n):
        name, limit = input().split()
        limit = int(limit)
        title.append((name, limit))

    for _ in range(m):
        power = int(input())
        result = 0
        start, end = 0, n
        while start <= end:
            mid = (start + end) // 2
            if power <= title[mid][1]:
                result = title[mid][0]
                end = mid - 1
            else:
                start = mid + 1
        print(result)