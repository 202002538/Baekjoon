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
        if a == b:
            return True
        if a > b:
            parent[a] = b
        else:
            parent[b] = a

    n, m = map(int, input().split())

    parent = [i for i in range(n+1)]
    cycle = 0
    for j in range(1, m+1):
        a, b = map(int, input().split())
        if union(parent, a, b) and not cycle:
            cycle = j
    print(cycle)