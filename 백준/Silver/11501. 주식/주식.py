import sys

if __name__ == '__main__':
    T = int(input())
    result = []

    for _ in range(T):
        N = int(sys.stdin.readline())
        nums = list(map(int, sys.stdin.readline().split()))
        nums.reverse()

        total = 0
        highest = 0
        for n in nums:
            if n > highest:
                highest = n
            else:
                total += highest-n
        result.append(total)

    print(*result)