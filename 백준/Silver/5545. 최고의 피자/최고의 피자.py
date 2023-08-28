if __name__ == '__main__':
    N = int(input())
    A, B = map(int, input().split(" "))
    C = int(input())
    kal = []

    for i in range(N):
        kal.append(int(input()))
    kal = sorted(kal, reverse=True)

    # 가장 비싼 토핑부터 하나씩
    cost = A
    total_kal = C #도우의 칼로리와 가격
    best = [total_kal//cost]

    for k in kal:
        cost += B
        total_kal += k
        best.append(total_kal//cost)

    print(max(best))
