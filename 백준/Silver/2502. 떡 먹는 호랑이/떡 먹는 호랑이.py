import sys
input = sys.stdin.readline

if __name__ == '__main__':
    d, k = map(int, input().split())
    a, b = 1, 1 #첫째날, 둘째날의 떡 개수
    dp = [0] * (d + 1)

    while True:
        dp[1], dp[2] = a, b

        #dp를 이용해서 d일차의 떡 개수 계산
        for i in range(3, d+1):
            dp[i] = dp[i-1] + dp[i-2]

        #떡 개수를 보고 a, b조정
        if dp[d] == k:
            print(a)
            print(b)
            break
        elif dp[d] < k:
            b += 1
        else:
            a += 1
            b = a