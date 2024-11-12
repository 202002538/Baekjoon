import sys
input = sys.stdin.readline
from collections import Counter

if __name__ == '__main__':
    for _ in range(int(input())):
        n = int(input())
        team = list(map(int, input().split()))
        dic = dict(Counter(team))

        for k in list(dic.keys()):
            if dic[k] >= 6:
                dic[k] = []
            else:
                dic.pop(k)

        score = 1
        for t in team:
            if t in dic.keys():
                dic[t].append(score)
                score += 1

        winner = []
        for k in dic.keys():
            winner.append([k, sum(dic[k][:4]), dic[k][4]])
        winner.sort(key=lambda x: (x[1], x[2]))

        print(winner[0][0])