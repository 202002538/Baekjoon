import sys
input = sys.stdin.readline

if __name__ == '__main__':
    for _ in range(int(input())):
        n, k, t, m = map(int, input().split())

        score = [[0] * (k+1) for _ in range(n+1)]
        submit_last = [0] * (n+1)
        submit_time = [0] * (n+1)
        
        for now in range(m):
            i, j, s = map(int, input().split())
            score[i][j] = max(score[i][j], s)
            submit_last[i] = now
            submit_time[i] += 1

        teams = []
        for a in range(1, n+1):
            teams.append([a, sum(score[a]), submit_time[a], submit_last[a]])
        teams.sort(key=lambda x: (-x[1], x[2], x[3]))

        for a in range(0, n):
            if teams[a][0] == t:
                print(a+1)