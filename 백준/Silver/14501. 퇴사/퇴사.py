import sys
input = sys.stdin.readline

if __name__ == '__main__':
    n = int(input())
    cons = []
    for _ in range(n):
        t, p = map(int, input().split())
        cons.append((t, p))

    dp = [0] * (n+1)

    max_value = 0
    for i in range(n-1, -1, -1):
        time = cons[i][0] + i
        if time <= n:
            dp[i] = max(cons[i][1] + dp[time], max_value)
            max_value = dp[i]
        else:
            dp[i] = max_value
    
    print(max_value)