INF= 1e9
import sys
input = sys.stdin.readline

def solution(N, number):
    answer = 0
    dp = [set() for _ in range(9)]

    # N, NN, NNN, ...에 대해 사용한 횟수 채우기
    num = N
    for i in range(1, 9):
        if num == number:
            return i
        dp[i].add(num)
        num += 10 ** i * N

    for i in range(1, 9):
        for j in range(1, i):
            for x in dp[j]: # 4 = (1+3), (2*2)
                for y in dp[i-j]:
                    dp[i].add(x*y)
                    dp[i].add(x+y)
                    dp[i].add(x-y)
                    if y != 0:
                        dp[i].add(x//y)

                    if number in dp[i]:
                        return i
    return -1