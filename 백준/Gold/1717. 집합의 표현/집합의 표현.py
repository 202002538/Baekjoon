import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)


if __name__ == '__main__':
    n, m = map(int, input().split())
    parent = [i for i in range(n+1)]

    def union(a, b):
        a = find_parent(a)
        b = find_parent(b)
        if a < b: 
            parent[b] = a
        else:
            parent[a] = b

    def find_parent(a):
        if parent[a] != a:
            parent[a] = find_parent(parent[a])
        return parent[a]

    for _ in range(m):
        num, x, y = map(int, input().split())
        if num == 0:
            union(x, y)
        else:
            if find_parent(x) == find_parent(y):
                print("YES")
            else:
                print("NO")