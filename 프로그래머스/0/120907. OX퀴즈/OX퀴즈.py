def solution(quiz):
    answer = []
    for q in quiz:
        exp, ans = q.split(" = ")
        answer.append('O') if eval(exp) == int(ans) else answer.append('X')
    return answer