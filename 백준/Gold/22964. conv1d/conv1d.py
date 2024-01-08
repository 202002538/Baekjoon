import sys
input = sys.stdin.readline

if __name__ == '__main__':
    n, k, x = map(int, input().split())

    tmp = [0] * x
    for i in range(x):
        tmp[i] = i+1

    num = sum(tmp) * sum(tmp) * x**(n+k-2) * k
    num %= 998244353

    for _ in range(n-k+1):
        print(num, end=" ")