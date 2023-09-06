import heapq
import sys
input = sys.stdin.readline
INF = float('inf')

if __name__ == '__main__':
    n, m, k = map(int, input().split())
    graph = [[] for _ in range(n+1)]
    for _ in range(m):
        a, b, c = map(int, input().split())
        graph[b].append((a, c)) #reverse로 저장!!
    place = list(map(int, input().split()))


    # 다익스트라 세팅
    distance = [INF] * (n + 1)
    hq = []
    
    # 모든 면접장의 초기값을 0으로 두고 시작
    for p in place:
        distance[p] = 0
        heapq.heappush(hq, (0, p))

    while hq:
        dis, now = heapq.heappop(hq)
        if dis > distance[now]:
            continue
        for j in graph[now]:
            temp = dis + j[1]
            if temp < distance[j[0]]:
                distance[j[0]] = temp
                heapq.heappush(hq, (temp, j[0]))

    far = max(distance[1:])
    print(distance.index(far))
    print(far)