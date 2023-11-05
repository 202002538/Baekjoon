import sys
input = sys.stdin.readline

if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    result = 0
    for i in range(n):
        if a[i] > b[i]:
            result += a[i] - b[i]
    print(result)