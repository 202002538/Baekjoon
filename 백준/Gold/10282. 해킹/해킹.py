import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

if __name__ == '__main__':
    result = []
    case = int(input())
    for _ in range(case):
        n, d, c = map(int, input().split())
        graph = [[] for _ in range(n+1)]
        for _ in range(d):
            a, b, s = map(int, input().split())
            graph[b].append((a, s))

        #최소 시간 저장
        distance = [INF] * (n+1)

        #시작점 세팅
        distance[c] = 0
        hq = []
        heapq.heappush(hq, (0, c))

        #다익스트라
        while hq:
            dis, now = heapq.heappop(hq)
            if dis > distance[now]:
                continue
            for i in graph[now]:
                temp = dis + i[1]
                if temp < distance[i[0]]:
                    distance[i[0]] = temp
                    heapq.heappush(hq, (temp, i[0]))

        #감염된 수와 마지막 감염시간 저장
        count = 0
        lastest = 0
        for j in distance:
            if j != INF:
                count += 1
                lastest = max(lastest, j)
        result.append([count, lastest])

    #최종결과 프린트
    for k in result:
        print(*k)
