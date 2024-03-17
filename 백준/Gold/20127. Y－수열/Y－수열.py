INF = int(1e9)
import sys
input = sys.stdin.readline

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    asc_sort = sorted(arr.copy())
    des_sort = sorted(arr.copy(), reverse=True)

    def asc_arr(array):
        count, idx = 0, 0
        for a in range(len(array)-1):
            if array[a] > array[a+1]: #감소구간 체크
                count += 1
                idx = a+1
        if count == 1 and array[0] >= arr[-1]:
            return idx
        else:
            return INF

    def des_arr(array):
        count, idx = 0, 0
        for a in range(len(array)-1):
            if array[a] < array[a+1]: #증가구간 체크
                count += 1
                idx = a+1
        if count == 1 and array[0] <= arr[-1]:
            return idx
        else:
            return INF

    k = INF
    if arr == asc_sort or arr == des_sort:
        k = 0
    else:
        k = min(k, asc_arr(arr))
        k = min(k, des_arr(arr))

    print(k) if k != INF else print(-1)