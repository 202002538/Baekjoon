import sys
input = sys.stdin.readline

if __name__ == '__main__':
    n = int(input())
    med = [-1] * 101

    for _ in range(n):
        effect, num = map(int, input().split())
        med[effect] = num

    r = int(input())
    for _ in range(r):
        result = []
        for s in list(map(int, input().split()))[1:]:
            if med[s] != -1:
                result.append(med[s])
            else:
                result = ["YOU DIED"]
                break
        print(*result)