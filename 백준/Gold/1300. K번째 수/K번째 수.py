import sys
input = sys.stdin.readline

if __name__ == '__main__':
    n = int(input())
    k = int(input())

    start, end = 0, k
    result = 0

    while start <= end:
        mid = (start + end) // 2

        #숫자 mid가 행렬 A에서 몇번째 수인지 파악
        count = sum(min(n, mid // i) for i in range(1, n+1))

        if count >= k:
            result = mid
            end = mid - 1
        else:
            start = mid + 1

    print(result)
