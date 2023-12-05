import sys
input = sys.stdin.readline

if __name__ == '__main__':
    nums = list(map(int, input().split()))
    now = min(nums)
    not_find = True
    while not_find:
        check = 0
        for n in nums:
            if now % n == 0:
                check += 1
            if check >= 3:
                print(now)
                not_find = False
                break
        else:
            now += 1