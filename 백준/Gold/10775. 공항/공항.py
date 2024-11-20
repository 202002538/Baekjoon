import sys
input = sys.stdin.readline

g = int(input())
p = int(input())

def find(a):
    if parent[a] != a:
        parent[a] = find(parent[a])
    return parent[a]

def union(a, b):
    a = find(a)
    b = find(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

result = 0
parent = [i for i in range(g+1)]
for _ in range(p):
    num = int(input())
    gate = find(num)
    if gate == 0:
        break
    union(gate, gate-1)
    result += 1
print(result)