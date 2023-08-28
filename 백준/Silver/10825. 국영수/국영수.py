import sys
input = sys.stdin.readline

if __name__ == '__main__':
    n = int(input())
    student = []
    for _ in range(n):
        name, kor, eng, math = input().split()
        student.append((name, int(kor), int(eng), int(math)))

    student.sort(key=lambda x: (-x[1], x[2], -x[3], x[0]))

    for s in student:
        print(s[0])