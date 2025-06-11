num = {'-': 0, '\\': 1, '(': 2, '@': 3, '?': 4,
       '>': 5, '&': 6, '%': 7, '/': -1}

while True:
    a = list(input())
    if a[0] == '#':
        break

    mul, count = 0, 0
    for i in range(len(a)-1, -1, -1):
        count += 8 ** mul * num[a[i]]
        mul += 1
    print(count)