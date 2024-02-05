import sys
input = sys.stdin.readline

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))

    summ = [0] * n
    summ[0] = arr[0]
    for i in range(1, n):
       summ[i] = summ[i-1] + arr[i]

    case1 = 0
    for i in range(1, n-1):
        honey = (summ[n-1] - summ[0] - arr[i]) + (summ[n-1] - summ[i])
        case1 = max(case1, honey)
    case2 = 0
    for i in range(1, n-1):
        honey = (summ[n-2] - arr[i]) + (summ[i-1])
        case2 = max(case2, honey)
    case3 = 0
    for i in range(1, n-1): #i가 벌통위치
        honey = (summ[i] - arr[0]) + (summ[n-2] - summ[i-1])
        case3 = max(case3, honey)

    print(max(case1, case2, case3))