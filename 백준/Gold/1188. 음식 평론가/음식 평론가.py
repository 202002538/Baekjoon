import sys
input = sys.stdin.readline
import math

if __name__ == '__main__':
    n, m = map(int, input().split())
    print(m - math.gcd(n, m))