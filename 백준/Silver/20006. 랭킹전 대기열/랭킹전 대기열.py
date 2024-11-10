import sys
input = sys.stdin.readline

if __name__ == '__main__':
    p, m = map(int, input().split())
    # (처음 플레이어의 렙, 이름 - 차별성 두기): [(렙, 이름), ...]
    room = {} 
    for _ in range(p):
        l, n = input()[:-1].split()
        l = int(l)
        for k in room.keys():
            if abs(k[0] - l) <= 10 and len(room[k]) < m:
                room[k].append([l, n])
                break
        else: #들어간 방 없으면 새로 만들기
            room[(l, n)] = [[l, n]]

    for k in room.keys():
        print("Started!") if len(room[k]) == m else print("Waiting!")
        room[k].sort(key=lambda x: x[1])
        for lev, name in room[k]:
            print(lev, name)
