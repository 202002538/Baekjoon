import sys
input = sys.stdin.readline

if __name__ == '__main__':
    n = int(input())
    mem = [0]
    for _ in range(n):
        mem.append(int(input()))
    mem.sort()

    hacker = 0
    for i in range(n):
        diff = mem[i+1] - mem[i]
        if diff > 1:
            hacker += diff-1
            mem[i+1] = mem[i]+1
    print(hacker)