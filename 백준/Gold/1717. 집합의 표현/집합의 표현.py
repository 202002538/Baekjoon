import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

if __name__ == '__main__':
    def find(parent, x):
        if parent[x] != x:
            parent[x] = find(parent, parent[x])
        return parent[x]

    def union(parent, a, b):
        a = find(parent, a)
        b = find(parent, b)
        if a < b:
            parent[b] = a
        else:
            parent[a] = b

    #입력 및 초기화
    n, m = map(int, input().split())
    parent = [i for i in range(n+1)] #부모 배열 초기화

    for _ in range(m):
        op, a, b = map(int, input().split())
        if op == 0:
            union(parent, a, b)
        else:
            if find(parent, a) == find(parent, b):
                print("YES")
            else:
                print("NO")