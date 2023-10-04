import sys
input = sys.stdin.readline

if __name__ == '__main__':
    dir = ['N', 'E', 'S', 'W']
    now = 0
    for _ in range(10):
        command = int(input())
        if command == 1:
            now = (now+1) % 4
        elif command == 2:
            now = (now+2) % 4
        else:
            now = (now-1) % 4
    print(dir[now])