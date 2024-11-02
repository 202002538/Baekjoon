def solution(lines):
    num = []
    stacked = set()
    for s, e in lines:
        for i in range(s, e):
            if i not in num:
                num.append(i)
            else:
                stacked.add(i)
    return len(stacked)