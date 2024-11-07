import sys
input = sys.stdin.readline
INF = 2e9

if __name__ == '__main__':
    n = int(input())
    nums = list(map(int, input().split()))

    start, end = 0, n-1
    summ = INF
    result = []
    while start < end:
        tmp = nums[start] + nums[end]
        if tmp == 0:
            result = [nums[start], nums[end]]
            break
        elif summ > abs(tmp): 
            summ = abs(tmp)
            result = [nums[start], nums[end]]
        if tmp < 0: 
            start += 1
        elif tmp > 0: 
            end -= 1
    print(*result)