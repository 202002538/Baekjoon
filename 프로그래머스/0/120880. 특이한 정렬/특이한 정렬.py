def solution(numlist, n):
    answer = []
    for num in numlist:
        answer.append((abs(n-num), num))

    answer = sorted(answer, key=lambda x:(x[0], -x[1]))
    answer = list(map(lambda x: x[1], answer))
    return answer