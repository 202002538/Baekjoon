import sys
input = sys.stdin.readline

if __name__ == '__main__':
    k, n = map(int, input().split())
    lan = [int(input()) for _ in range(k)]

    start, end = 0, 2**31-1
    result = 0

    while start <= end:
        mid = (start + end) // 2
        count = sum(x//mid for x in lan)

        if count < n:
            end = mid - 1
        else:
            result = mid
            start = mid + 1
    print(result)