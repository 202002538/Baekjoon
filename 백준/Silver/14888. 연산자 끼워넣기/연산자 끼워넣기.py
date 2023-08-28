import sys
input = sys.stdin.readline

if __name__ == '__main__':
    n = int(input())
    nums = list(map(int, input().split()))
    add, sub, mul, div = map(int, input().split())

    min_v = 1e10
    max_v = -1e10

    def dfs(i, now):
        global min_v, max_v, add, sub, mul, div
        if i == n:
            min_v = min(min_v, now)
            max_v = max(max_v, now)
        else:
            if add > 0:
                add -= 1
                dfs(i+1, now + nums[i])
                add += 1
            if sub > 0:
                sub -= 1
                dfs(i + 1, now - nums[i])
                sub += 1
            if mul > 0:
                mul -= 1
                dfs(i+1, now * nums[i])
                mul += 1
            if div > 0:
                div -= 1
                dfs(i+1, int(now / nums[i]))
                div += 1

    dfs(1, nums[0])
    print(max_v)
    print(min_v)