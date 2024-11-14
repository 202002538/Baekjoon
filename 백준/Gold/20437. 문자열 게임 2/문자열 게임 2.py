import sys
input = sys.stdin.readline
from collections import Counter

for _ in range(int(input())):
    w = list(input()[:-1])
    k = int(input())

    dic = dict(Counter(w))
    for i in list(dic.keys()):
        if dic[i] < k:
            dic.pop(i)
        else:
            dic[i] = []
    if not dic:
        print(-1)
        
    else:
        for i, word in enumerate(w):
            if word in dic.keys():
                dic[word].append(i)
    
        mini, maxi = 1e6, 0
        for i in dic.keys():
            for j in range(len(dic[i])-k+1):
                distance = dic[i][j+k-1] - dic[i][j] + 1
                mini = min(mini, distance)
                maxi = max(maxi, distance)
    
        print(mini, maxi)