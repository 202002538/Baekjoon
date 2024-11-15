import sys
input = sys.stdin.readline

n = int(input())
words = []
for i in range(n):
    words.append(input()[:-1])

def check(a, b):
    count = 0
    for i in range(min(len(a), len(b))):
        if a[i] == b[i]:
            count += 1
        else:
            break
    return count

maxlen = 0
tmp = []
for i in range(n):
    for j in range(i+1, n):
        if words[i][0] != words[j][0]:
            continue
        count = check(words[i], words[j])
        if count > maxlen:
            maxlen = count
            tmp = [words[i], words[j]]

print(tmp[0])
print(tmp[1])
