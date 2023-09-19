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
        if a > b:
            parent[a] = b
        else:
            parent[b] = a

    #input
    g = int(input())
    p = int(input())
    parent = [i for i in range(g+1)]

    #번호 확인
    result = 0
    for i in range(p):
        num = int(input())
        root = find(parent, num) #루트 노드는 "현재 도킹가능한 가장 큰 번호"
        if root == 0: #도킹 가능한 자리x
            break
        union(parent, root, root-1) #도킹완료. 루트노드를 1 줄인다.
        result += 1

    print(result)