import sys
input = sys.stdin.readline

if __name__ == '__main__':
    n = int(input())
    man = []
    for _ in range(n):
        x, y = map(int, input().split())
        man.append((x, y))

    result = []
    for i in range(n):
        bigger = 0
        for j in range(n):
            if man[j][0] > man[i][0] and man[j][1] > man[i][1]:
                bigger += 1
        result.append(bigger+1)
    print(*result)