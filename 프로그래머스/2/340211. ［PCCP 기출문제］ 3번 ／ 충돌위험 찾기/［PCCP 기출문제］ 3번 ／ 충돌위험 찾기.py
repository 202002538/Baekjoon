import sys
input = sys.stdin.readline
from collections import Counter

def solution(points, routes):
    path = []

    for i in range(len(routes)):
        time = 0
        x, y = points[routes[i][0]-1]
        path.append((x, y, 0))
        for j in range(len(routes[i])-1):
            x1, y1 = points[routes[i][j]-1]
            x2, y2 = points[routes[i][j+1]-1]
            while x1 != x2 or y1 != y2:
                time += 1
                if x1 < x2:
                    x1 += 1
                elif x1 > x2:
                    x1 -= 1
                elif y1 < y2:
                    y1 += 1
                elif y1 > y2:
                    y1 -= 1
                path.append((x1, y1, time))
    
    answer = 0
    counter = Counter(path)
    for v in counter.values():
        if v >= 2:
            answer += 1
    return answer