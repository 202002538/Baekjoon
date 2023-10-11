import sys
input = sys.stdin.readline

if __name__ == '__main__':
    n = int(input())
    hw = []
    day = 0
    for _ in range(n):
        d, t = map(int, input().split())
        hw.append((d, t, t-d)) #t-d일 내 시작해야 마감을 맞출 수 있음
        day = max(day, t)
    hw.sort(key=lambda x: (x[1], -x[2]))

    while hw:
        #마감이 제일 늦으면서 빨리 시작해야 하는것 부터 계획에 넣기
        d, t, last = hw.pop()
        if day > t:
            day = t

        day -= d #해당 과제 시작 전날

    print(day)