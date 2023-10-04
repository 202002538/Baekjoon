import sys
input = sys.stdin.readline

if __name__ == '__main__':
    n = int(input())
    result = []
    for i in range(n):
        x, y, v = map(int, input().split())
        shot = (x**2 + y**2)**(1/2) / v
        result.append((i+1, shot))
    result.sort(key=lambda x:x[1])

    for r in result:
        print(r[0])