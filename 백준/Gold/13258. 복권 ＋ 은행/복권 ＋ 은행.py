import sys
input = sys.stdin.readline

if __name__ == '__main__':
    n = int(input())
    money = list(map(int, input().split()))
    price = int(input()) #당첨금액
    week = int(input()) #진행 주수

    #초기테이블 세팅
    dp = [[0] * (n + 1) for _ in range(week + 1)]
    dp[0][1:1+n] = money

    #dp
    for i in range(week):
        total = sum(dp[i])
        for j in range(n+1):
            #다음주 내 잔고에 "추가될 기대값" = (1/ 이번주 모든 사람의 잔고합) * 내 잔고 * 당첨금
            dp[i+1][j] = dp[i][j] + (1/total * dp[i][j] * price)

    print(dp[week][1]) #1번사람(강호)의 기댓값 출력
