import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

if __name__ == '__main__':
    def find(parent, x):
        if x != parent[x]:
            parent[x] = find(parent, parent[x])
        return parent[x]


    def union(parent, a, b):
        a = find(parent, a)
        b = find(parent, b)
        if well[a] > well[b]: #파는 비용이 더 저렴한 번호가 루트가 되게
            parent[a] = b
        else:
            parent[b] = a

    #input
    n = int(input())
    well, edges = [0], []
    for _ in range(n): #우물비용 입력
        well.append(int(input()))
    for i in range(1, n+1): #연결비용 입력
        connect = list(map(int, input().split()))
        for j, c in enumerate(connect):
            edges.append((c, i, j+1))
    edges.sort()

    #크루스칼
    result = 0
    parent = [i for i in range(n+1)]
    for edge in edges:
        c, a, b = edge
        if find(parent, a) != find(parent, b):
            if c > well[find(parent, a)] and c > well[find(parent, b)]:
                continue
            else:
                result += c
                union(parent, a, b)

    #최종 집합 개수 확인
    for i in range(n+1):
        find(parent, i)

    #만들어진 집합에 하나씩 우물 설치
    for root in set(parent[1:]):
        result += well[root]
    print(result)

