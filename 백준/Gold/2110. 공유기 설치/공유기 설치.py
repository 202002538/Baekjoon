import sys
input = sys.stdin.readline

if __name__ == '__main__':
    n, c = map(int, input().split())
    nums = [int(input()) for _ in range(n)]
    nums.sort()

    start = 1
    end = nums[-1] - nums[0]
    result = 0
    
    while start <= end:
        mid = (start + end) // 2

        wifi = 1
        now = nums[0]
        for n in nums[1:]:
            if n - now >= mid: 
                wifi += 1
                now = n

        if wifi < c: 
            end = mid - 1
        else:        
            result = mid
            start = mid + 1

    print(result)