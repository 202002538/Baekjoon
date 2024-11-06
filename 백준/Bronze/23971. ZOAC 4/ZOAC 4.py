import sys
input = sys.stdin.readline
import math

if __name__ == '__main__':
    h, w, n, m = map(int, input().split())
    depth = math.ceil(h / (n+1))
    width = math.ceil(w / (m+1))
    print(depth * width)