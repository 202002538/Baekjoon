import sys
input = sys.stdin.readline

n, d = map(int, input().split())
dp = [i for i in range(d+1)]
short = {}
for _ in range(n):
    s, e, dis = map(int, input().split())
    if s < 0 or e > d:
        continue
    if s in short.keys():
        short[s].append((e, dis))
    else:
        short[s] = [(e, dis)]

if 0 in short.keys():
    for e, dis in short[0]:
        dp[e] = min(dp[e], dp[0] + dis)

for i in range(1, d+1):
    dp[i] = min(dp[i - 1] + 1, dp[i])
    if i in short.keys():
        for e, dis in short[i]:
            dp[e] = min(dp[e], dp[i] + dis)
print(dp[-1])