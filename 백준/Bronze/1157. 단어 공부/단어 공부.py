import sys
input = sys.stdin.readline
from collections import Counter

if __name__ == '__main__':
    words = input()[:-1]
    words = words.upper()

    words = Counter(words).most_common(2)
    if len(words) > 1 and words[0][1] == words[1][1]:
        print("?")
    else:
        print(words[0][0])