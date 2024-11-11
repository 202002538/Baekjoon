import sys
input = sys.stdin.readline

if __name__ == '__main__':
    strr = input()[:-1]
    bomb = list(input()[:-1])
    n = len(bomb)

    stack = []
    for s in strr:
        stack.append(s)
        if stack[-n:] == bomb:
            del stack[-n:]

    print(''.join(stack)) if stack else print("FRULA")