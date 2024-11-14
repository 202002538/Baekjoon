import sys
input = sys.stdin.readline

n = int(input())
channel = []
for _ in range(n):
    channel.append(input()[:-1])

click = []
idx1 = channel.index("KBS1")
idx2 = channel.index("KBS2")

if idx1 > idx2:
    idx2 += 1

click.extend(['1'] * idx1)
click.extend(['4'] * idx1)

if idx2 != 1:
    click.extend(['1'] * idx2)
    click.extend(['4'] * (idx2-1))

print(''.join(click))