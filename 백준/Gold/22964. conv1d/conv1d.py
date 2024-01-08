import sys
input = sys.stdin.readline

if __name__ == '__main__':
    n, k, x = map(int, input().split())

    num = x*(x+1)//2 * x*(x+1)//2 * x**(n+k-2) * k
    num %= 998244353

    for _ in range(n-k+1):
        print(num, end=" ")