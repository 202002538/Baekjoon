import sys
input = sys.stdin.readline

if __name__ == '__main__':
    n = int(input())
    sol = list(map(int, input().split()))

    sol.sort(key=lambda x: abs(x))
    minimum = 2e10
    a, b = 0, 0

    for i in range(n-1):
        summ = abs(sol[i] + sol[i+1])
        if summ == 0:
            a, b = sol[i], sol[i+1]
            break
        if summ < minimum:
            minimum = summ
            a, b = sol[i], sol[i + 1]

    print(a, b) if a < b else print(b, a)