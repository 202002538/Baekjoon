import sys
input = sys.stdin.readline
if __name__ == '__main__':
    n = int(input())
    count = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    d = [0] * (n+1)
    d[1] = 9

    for i in range(2, n+1):
        tmp = [0] * 10
        d[i] = (2 * d[i-1] - (count[0] + count[9])) % 1000000000

        tmp[0] = count[1]
        tmp[9] = count[8]
        for j in range(1, 9):
            tmp[j] = count[j-1] + count[j+1]
        count = tmp

    print(int(d[n]))