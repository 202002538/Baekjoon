INF = int(1e9)
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

if __name__ == '__main__':
    n = int(input())
    pringles = []
    for _ in range(n):
        s, e = map(int, input().split())
        pringles.append((s, e))

    def greedy(stress):
        stress_list = [stress] #스트레스 변화 과정
        reduce = 0 #줄어든 수명
        for i in range(1, n): #프링글스를 2번째 통부터 순서대로 먹는다.
            s, e = pringles[i]
            if stress < s: 
                reduce += abs(stress - s)
                stress = s
            elif stress > e: 
                reduce += abs(stress - e)
                stress = e 
            stress_list.append(stress)
        return reduce, stress_list

    result, tmp = INF, []
    for g in range(pringles[0][0], pringles[0][1]+1): #스트레스 시작점 -> 첫번째 통으로 가능한 모든 범위
        r, l = greedy(g)
        if result > r: #줄어든 수명 최대한 작은 경우 저장
            result = r
            tmp = l
            
    print(result)
    for t in tmp:
        print(t)