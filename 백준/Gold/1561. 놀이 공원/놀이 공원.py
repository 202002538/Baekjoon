import sys
input = sys.stdin.readline

if __name__ == '__main__':
    n, m = map(int, input().split())
    time = list(map(int, input().split()))

    if n <= m:
        print(n)
    else:
        min_time = 0
        start = 0
        end = max(time) * n

        while start <= end:
            mid = (start + end) // 2
            count = m
            count += sum(mid // t for t in time)
            if count < n:
                start = mid + 1
            else:
                min_time = mid
                end = mid - 1

        now = m
        now += sum((min_time - 1) // t for t in time)
        n -= now

        for i, t in enumerate(time):
            if min_time % t == 0:
                n -= 1
            if n == 0:
                print(i + 1)
                break