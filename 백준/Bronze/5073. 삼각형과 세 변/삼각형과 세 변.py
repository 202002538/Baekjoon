import sys
input = sys.stdin.readline

if __name__ == '__main__':
    while True:
        nums = list(map(int, input().split(" ")))
        if nums[0] == 0:
            break
            
        nums.sort()
        if nums[2] >= nums[0] + nums[1]:
            print("Invalid")
            continue
        elif nums[0] == nums[1] == nums[2]:
            print("Equilateral")
            continue
        elif nums[0] == nums[1] or nums[1] == nums[2]:
            print("Isosceles")
            continue
        else:
            print("Scalene")