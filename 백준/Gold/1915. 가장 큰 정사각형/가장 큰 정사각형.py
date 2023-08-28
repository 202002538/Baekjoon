import sys
input = sys.stdin.readline
if __name__ == '__main__':
    n, m = map(int, input().split())
    s = [[0] * (m+1)]
    for _ in range(n):
        s.append([0] + list(map(int, list(input()[:-1]))))

    large = 0
    for i in range(1, n+1):
        for j in range(1, m+1):
            if s[i][j] != 0:
                s[i][j] = min(s[i][j-1], s[i-1][j-1], s[i-1][j]) + 1
                large = max(large, s[i][j])
    print(large**2)