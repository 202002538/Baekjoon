st = list(map(int, input().split()))
q = int(input())

for _ in range(q):
    now = list(map(int, input().split()))
    x, y = now[0], now[1]
    now = now[2:]
    result = []

    for i in range(3):
        m = abs(x - st[2 * i]) + abs(y - st[2 * i + 1])
        tmp = ((m + now[i] - 1) // now[i]) * now[i]
        result.append(tmp)

    print(min(result))