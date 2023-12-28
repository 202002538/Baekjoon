import sys
input = sys.stdin.readline

if __name__ == '__main__': 
    n, m, k = map(int, input().split())
    money = [0] + list(map(int, input().split()))

    #다른 집합의 최소비용 친구를 선택
    parent = [0] * (n+1)
    for i in range(n+1):
        parent[i] = i

    def union(parent, x, y):
        #비용 더 적은애가 부모가 되도록 합집합
        a, b = find(parent, x), find(parent, y)
        if a == b:
            return
        if money[a] <= money[b]:
            parent[b] = a
        else:
            parent[a] = b

    def find(parent, x):
        if parent[x] != x:
            parent[x] = find(parent, parent[x])
        return parent[x]

    for _ in range(m):
        v, w = map(int, input().split())
        union(parent, v, w)

    #부모 노드 확인
    for i in range(n+1):
        find(parent, i)

    # 부모들을 합집합 -> 최소비용<가진비용이면 성공
    parents = set(parent[1:])
    result = 0
    for p in parents:
        result += money[p]

    if result <= k:
        print(result)
    else:
        print("Oh no")