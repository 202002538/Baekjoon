import sys
input = sys.stdin.readline

if __name__ == '__main__':
    a, b = map(int, input().split())
    result = []

    if b >= a:
        print('NO')
    elif a//2 > b:
        print('NO')
    else:
        while (b // 2 + 1) * 2 != a and b+1 != a:
            result.append('aba')
            a -= 2
            b -= 1
        if a != 0 and b != 0:
            if b + 1 == a:
                tmp = 'a' + 'ba' * b
                result.append(tmp)
            elif (b // 2 + 1) * 2 == a:
                tmp = 'a' + 'ba' * (b//2)
                result.append(tmp)
                result.append(tmp)
            if len(result) != 0:
                print('YES')
                print(len(result))
                for r in result:
                    print(r)
            else:
                print('NO')
        else:
            print('NO')