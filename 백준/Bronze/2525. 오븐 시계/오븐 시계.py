if __name__ == '__main__':
    h, m = map(int, input().split())
    need = int(input())

    if m + need >= 60:
        h = (h + (m + need) // 60) % 24
        m = (m + need) % 60
    else:
        m += need

    print(h, m)