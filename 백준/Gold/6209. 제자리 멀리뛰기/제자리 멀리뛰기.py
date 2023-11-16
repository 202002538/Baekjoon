import sys
input = sys.stdin.readline

if __name__ == '__main__':
    d, n, m = map(int, input().split())
    isle = [0]
    for _ in range(n):
        isle.append(int(input()))
    isle.append(d)
    isle.sort()

    #이분탐색
    start = 0
    end = d - 0
    result = 0
    while start <= end:
        mid = (start + end) // 2 #점프가능 최소거리

        #스킵해야하는 개수 카운트
        count = 0
        now = 0
        for i in range(n+1):
            if isle[i+1] - now < mid: 
                count += 1
            else:
                now = isle[i+1]

        if count <= m: 
            result = mid
            start = mid + 1
        else:
            end = mid - 1
    print(result)