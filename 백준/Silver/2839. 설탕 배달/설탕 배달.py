if __name__ == '__main__':
    N = int(input())
    count = 0
    while N > 0 and N % 5 != 0:
        count += 1
        N -= 3
    count += N//5
    N %= 5

    print(count if N == 0 else -1)