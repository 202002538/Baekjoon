INF = int(1e9)
import sys
input = sys.stdin.readline

if __name__ == '__main__':
    n, s = map(int, input().split())
    nums = list(map(int, input().split()))

    for i in range(n-1): #누적합
        nums[i+1] += nums[i]
    nums = [0] + nums

    start = 1
    end = 1
    result = INF
    while start <= end and end <= n:
        total = nums[end] - nums[start-1]
        if total >= s:
            result = min(result, end-start+1)
            start += 1
        else:
            end += 1
    print(0) if result == INF else print(result)