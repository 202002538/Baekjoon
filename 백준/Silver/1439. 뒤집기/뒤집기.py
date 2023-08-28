if __name__ == '__main__':
    nums = list(map(int, [s for s in input()]))

    count = 0
    now = nums[0]

    for n in nums[1:]:
        if now != n:
            count += 1
        now = n

    print((count+1) // 2)