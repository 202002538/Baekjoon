def solution(polynomial):
    poly = polynomial.split(' ')
    a, b = 0, 0
    for p in poly:
        if p == '+':
            continue
        if p[-1] == 'x':
            if p == 'x':
                a += 1
            else:
                a += int(p[:-1])
        else:
            b += int(p)
    
    answer = ''
    if a > 0:
        if a != 1:
            answer += str(a)
        answer += 'x'
    if b > 0:
        if answer != '':
            answer += ' + '
        answer += str(b)
    return answer