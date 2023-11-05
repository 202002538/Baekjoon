import sys
input = sys.stdin.readline

if __name__ == '__main__':
    a, b = map(int, input().split())
    result = min(a + a - 1, b + b + 1)
    print(result)