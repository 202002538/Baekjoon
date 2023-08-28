import sys
input = sys.stdin.readline

if __name__ == '__main__':
    n, g, k = map(int, input().split())
    ess, non_ess = [], []
    for _ in range(n):
        s, l, o = map(int, input().split())
        if o == 1:
            non_ess.append([s, l])
        else:
            ess.append([s, l])

    start, end = 0, 2e9
    result = 0
    while start <= end:
        mid = (start + end) // 2
        count = sum(s * max(1, mid - l) for s, l in ess)
        if len(non_ess) > k:
            non_ess.sort(key=lambda x: -x[0]*max(1, mid-x[1]))
            count += sum(s * max(1, mid - l) for s, l in non_ess[k:])

        if count > g:
            end = mid - 1
        else:
            result = mid
            start = mid + 1

    print(int(result))