import sys
input = sys.stdin.readline

def solution(diffs, times, limit):
    start, end = 1, 10**15
    answer = 0

    while start <= end: #이진탐색
        mid = (start + end) // 2
        
        time = 0
        for i in range(len(diffs)):
            if diffs[i] <= mid:
                time += times[i]
            else:
                time += (diffs[i] - mid) * (times[i] + times[i-1])
                time += times[i]

        if time > limit:
            start = mid + 1
        else: #제한시간내 퍼즐 해결 -> mid값 기록해둠
            answer = mid
            end = mid - 1

    return answer