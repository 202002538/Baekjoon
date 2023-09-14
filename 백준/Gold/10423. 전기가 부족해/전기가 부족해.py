import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)
from collections import deque

if __name__ == '__main__':
    def find(parent, x):
        if x != parent[x]:
            parent[x] = find(parent, parent[x])
        return parent[x]

    def union(parent, a, b): #합집합 시 발전소가 무조건 루트가 되게
        a = find(parent, a)
        b = find(parent, b)
        if a in power:
            parent[b] = a
        elif b in power:
            parent[a] = b
        else:
            if a > b:
                parent[a] = b
            else:
                parent[b] = a

    #input
    n, m, k = map(int, input().split())
    power = list(map(int, input().split()))
    edges = []
    for _ in range(m):
        a, b, c = map(int, input().split())
        edges.append((c, a, b))

    edges.sort()
    
    #크루스칼
    parent = [i for i in range(n+1)]
    result = 0
    for edge in edges:
        c, a, b = edge
        #양쪽이 속한 집합에 발전소가 있는지 확인, 둘 다 있으면 안됨
        #한쪽이라도 발전소가 없으면서 사이클이 아닌경우 합집합
        if find(parent, a) in power and find(parent, b) in power:
            continue
        elif find(parent, a) != find(parent, b):
            union(parent, a, b)
            result += c
    print(result)