INF = int(1e9)
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

if __name__ == '__main__':
    n = int(input())
    e = int(input())

    all_song = 0
    song = [[] for _ in range(n+1)] #아는 노래

    for i in range(e):
        campfire = list(map(int, input().split()))[1:]
        if 1 in campfire: #새로운 곡 출시
            all_song += 1
            for c in campfire:
                song[c].append(int(i))
        else: #곡 공유하는 날
            songs = []
            for c in campfire:
                songs += song[c]
            songs = list(set(songs)) #현재 참여자가 아는 모든 노래
            for c in campfire:
                song[c] = songs.copy()

    for i in range(n+1):
        if len(song[i]) == all_song:
            print(i)