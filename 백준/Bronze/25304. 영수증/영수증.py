if __name__ == '__main__':
    total = int(input())

    for i in range(int(input())):
        price, count = map(int, input().split())
        total -= price * count

    print("Yes" if total == 0 else "No")