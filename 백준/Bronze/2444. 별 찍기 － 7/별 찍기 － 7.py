a = int(input())
for i in range(a-1, -1, -1):
    print(" " * i + "*" * ((a-i) * 2 - 1))
for i in range(1, a):
    print(" " * i + "*" * ((a-i) * 2 - 1))