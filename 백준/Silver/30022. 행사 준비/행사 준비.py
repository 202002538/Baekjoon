import sys
input = sys.stdin.readline

if __name__ == '__main__':
    n, a, b = map(int, input().split())

    stuff = []
    for _ in range(n):
        p, q = map(int, input().split())
        stuff.append((p, q))
    stuff.sort(key=lambda x: -(x[1] - x[0]))

    result = 0
    for p, q in stuff:
        if a > 0:
            result += p
            a -= 1
        else:
            result += q
    print(int(result))