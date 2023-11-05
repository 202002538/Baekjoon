import sys
input = sys.stdin.readline

if __name__ == '__main__':
    n, m = map(int, input().split())
    booked = [[0, 0] for _ in range(n+1)]

    for _ in range(m):
        k, s, e = map(int, input().split())
        if s >= booked[k][1]:
            print("YES")
            booked[k][1] = e
        else:
            print("NO")