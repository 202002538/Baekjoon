import sys
input = sys.stdin.readline
INF = 1e9

if __name__ == '__main__':
    n, s = map(int, input().split())
    nums = list(map(int, input().split()))

    for i in range(1, n):
        nums[i] += nums[i-1]
    nums = [0] + nums

    start, end = 0, 1
    result = INF 
    while start <= end and end <= n:
        summ = nums[end] - nums[start]
        if summ >= s:
            result = min(result, end-start)
            start += 1 
        else:
            end += 1
    print(0) if result == INF else print(result)