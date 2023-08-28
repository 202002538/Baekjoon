import sys
input = sys.stdin.readline

if __name__ == '__main__':
    n, m, l = map(int, input().split())
    where = [0] + list(map(int, input().split())) + [l]
    where.sort()

    start, end = 1, l-1
    result = 0

    while start <= end:
        mid = (start + end) // 2
        count = 0
        for i in range(n+1):
            count += (where[i+1] - where[i] - 1) // mid

        if count > m:
            start = mid + 1
        else:
            result = mid
            end = mid - 1

    print(result)