import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)

if __name__ == '__main__': 
    n, m = map(int, input().split())
    tour = [[] for _ in range(n+1)]
    for _ in range(m):
        a, b = map(int, input().split())
        tour[a].append(b)
    s = int(input())
    fanclub = list(map(int, input().split()))

    not_meet = 0
    def dfs(n):
        global not_meet
        if len(tour[n]) != 0: #아직 여행 남음 -> 팬 안만나는 쪽 진행
            for t in tour[n]:
                if t not in fanclub:
                    dfs(t)
        else: #팬 안만나고 여행 종료
            not_meet = 1

    if 1 not in fanclub:
        dfs(1)
    print("yes") if not_meet else print("Yes")