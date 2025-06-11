while True:
    a = list(input())
    if len(a) == 1 and a[0] == '0':
        break

    num = len(a) // 2
    for i in range(1, num+1):
        if a[i-1] != a[-1 * i]:
            print("no")
            break
    else:
        print("yes")