INF = int(1e9)
import sys
input = sys.stdin.readline

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    asc_sort = sorted(arr.copy())
    dec_sort = sorted(arr.copy(), reverse=True)

    def asc_arr(arr1):
        a = 0
        while arr1[-2] <= arr1[-1] and arr1[-1] <= arr1[0]:
            a += 1
            first = arr1.pop(0)
            arr1 += [first]
        return a, arr1

    def des_arr(arr2):
        a = 0
        while arr2[-2] >= arr2[-1] and arr2[-1] >= arr2[0]:
            a += 1
            first = arr2.pop(0)
            arr2 += [first]
        return a, arr2

    k = INF
    if arr == asc_sort or arr == dec_sort:
        k = 0
    else:
        count, tmp = asc_arr(arr.copy())
        if tmp == asc_sort:
            k = min(k, count)
        else:
            count, tmp = asc_arr(arr[1:] + [arr[0]])
            if tmp == asc_sort:
                k = min(k, count+1)

        count, tmp = des_arr(arr.copy())
        if tmp == dec_sort:
            k = min(k, count)
        else:
            count, tmp = des_arr(arr[1:] + [arr[0]])
            if tmp == dec_sort:
                k = min(k, count+1)

    print(k) if k != INF else print(-1)

