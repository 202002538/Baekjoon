import sys
input = sys.stdin.readline

if __name__ == '__main__':
    n, m = map(int, input().split())
    keyword = set()
    for _ in range(n):
        keyword.add(input()[:-1])
    for _ in range(m):
        use = set(input()[:-1].split(","))
        keyword -= use
        print(len(keyword))