import sys
input = sys.stdin.readline

if __name__ == '__main__':
    m = int(input())
    s = set()
    for _ in range(m):
        inp = input()[:-1]
        if inp == 'all':
            s.clear()
            s.update([str(i) for i in range(1, 21)])
        elif inp == 'empty':
            s.clear()
        else:
            command, num = inp.split()
            if command == 'add':
                s.add(num)
            elif command == 'remove':
                s.discard(num)
            elif command == 'check':
                print(1) if num in s else print(0)
            else:
                if num in s:
                    s.remove(num)
                else:
                    s.add(num)