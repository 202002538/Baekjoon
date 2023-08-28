import sys
input = sys.stdin.readline

if __name__ == '__main__':
    x = int(input())

    start, end = 0, 2e8
    while start <= end:
        mid = (start + end) // 2 
        count = ((mid-1) * mid) // 2

        if count < x: 
            result = mid
            start = mid + 1
        else:
            end = mid - 1

    x -= int((result-1) * result) // 2
    result += 1

    if result % 2 == 1:
        print("{0}/{1}".format(x, int(result) - x))
    else:
        print("{0}/{1}".format(int(result) - x, x))