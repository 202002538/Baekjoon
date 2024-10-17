import sys
input = sys.stdin.readline
import heapq


def solution(k, n, reqs):
    answer = 0
    mentor = [[[[0 for _ in range(i)], 0] for i in range(n+1)] for _ in range(k+1)] 
    for r in reqs:
        request, time, category = r
        for i in range(1, n+1):
            fastest_end = heapq.heappop(mentor[category][i][0])
            if fastest_end <= request:
                heapq.heappush(mentor[category][i][0], request + time)
            else:
                start = fastest_end - request
                mentor[category][i][1] += start
                heapq.heappush(mentor[category][i][0], fastest_end + time)

    tmp = [1 for _ in range(k+1)]
    for i in range(n-k):
        minus = 0
        idx = 0
        for j in range(1, k+1):
            k_minus = mentor[j][tmp[j]][1] - mentor[j][tmp[j]+1][1]
            if k_minus > minus:
                minus = k_minus
                idx = j
        tmp[idx] += 1

    for i in range(1, k+1):
        answer += mentor[i][tmp[i]][1]

    return answer