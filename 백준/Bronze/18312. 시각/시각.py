if __name__ == '__main__':
    n, k = map(int, input().split())
    count = 0

    for h in range(n+1):
        if h < 10:
            h = '0' + str(h)
        for m in range(60):
            if m < 10:
                m = '0' + str(m)
            for s in range(60):
                if s < 10:
                    s = '0' + str(s)

                #문자열 확인
                if str(k) in str(h) or str(k) in str(m) or str(k) in str(s):
                    count += 1
    print(count)