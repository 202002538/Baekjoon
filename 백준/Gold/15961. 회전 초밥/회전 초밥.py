import sys
input = sys.stdin.readline
from collections import defaultdict

n, d, k, c = map(int, input().split())
sushi = []
for _ in range(n):
    sushi.append(int(input()))
sushi.extend(sushi[:k]) #k만큼 더 이어준다

#defaultdict - 초밥 종류별로 먹은 여부를 기록
dic = defaultdict(int)
dic[c] += 1

result = 0
left, right = 0, k
for i in range(k):
    dic[sushi[i]] += 1

while right < len(sushi):
    result = max(result, len(dic))
    #왼쪽 스시 뱉고 오른쪽 스시 먹기
    dic[sushi[left]] -= 1
    dic[sushi[right]] += 1
    
    #왼쪽 스시의 먹은 개수가 0이 됨 - dic에서 제거
    #dic에는 먹은 개수가 있는 스시만 남도록
    if dic[sushi[left]] == 0:
        dic.pop(sushi[left])
       
    left += 1
    right += 1

    if result == d:
        break

print(result)