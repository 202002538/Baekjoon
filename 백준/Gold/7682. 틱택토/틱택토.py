import sys
input = sys.stdin.readline

if __name__ == '__main__':
    def win(board, mark):
        b = list(board)
        for i in range(0, 7, 3):
            if mark == b[i] == b[i+1] == b[i+2]:
                return True
        for i in range(3):
            if mark == b[i] == b[i+3] == b[i+6]:
                return True
        if (mark == b[0] == b[4] == b[8]) \
                or (mark == b[2] == b[4] == b[6]):
            return True
        return False

    while True:
        ttt = input()
        if ttt[:-1] == "end":
            break

        xwin, owin = win(ttt, 'X'), win(ttt, 'O')
        xcount, ocount = ttt.count('X'), ttt.count('O')

        if xcount < ocount or xcount > ocount+1:
            print("invalid")
            continue
        if xcount == ocount:
            if not xwin and owin:
                print("valid")
                continue
        if xcount == ocount + 1:
            if xcount == 5 and not owin:
                print("valid")
                continue
            elif xwin and not owin:
                print("valid")
                continue
        print("invalid")