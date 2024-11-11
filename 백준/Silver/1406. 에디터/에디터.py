import sys
input = sys.stdin.readline
from collections import deque

if __name__ == '__main__':
    #커서를 기준으로 왼쪽,오른쪽 큐를 구분
    left = deque(input()[:-1])
    right = deque()
    for _ in range(int(input())):
        command = input()[:-1]
        if command[0] == 'L' and left:
            right.appendleft(left.pop())
        elif command[0] == 'D' and right:
            left.append(right.popleft())
        elif command[0] == 'B' and left:
            left.pop()
        elif command[0] == 'P':
            c, a = command.split()
            left.append(a)
    print(''.join(left + right))