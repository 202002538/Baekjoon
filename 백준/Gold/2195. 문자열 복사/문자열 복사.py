import sys
input = sys.stdin.readline
INF = int(1e9)

if __name__ == '__main__':
    s = input()
    p = input()

    result = 0
    while p:
        cut = 0
        for i in range(len(p)):
            # p의 앞부분 일부를 s에서 복붙해올 수 있는지 확인
            if p[:i] in s:
                cut = i
        if cut == 0:
            break

        p = p[cut:] #복붙해온만큼 잘라냄
        result += 1
    print(result)