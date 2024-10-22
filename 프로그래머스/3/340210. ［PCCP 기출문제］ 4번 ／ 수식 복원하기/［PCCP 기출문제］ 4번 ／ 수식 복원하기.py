import sys
input = sys.stdin.readline

def _10toN(n, q):
    rev_base = ''
    while n > 0:
        n, mod = divmod(n, q)
        rev_base += str(mod)
    return rev_base[::-1]

def solution(expressions):
    mystery = []
    nums = [2, 3, 4, 5, 6, 7, 8, 9]

    for e in expressions:
        exp = e.split(" ")
        a, op, b, c = exp[0], exp[1], exp[2], exp[4]
        #수식 내 가장 큰 수로 진법 범위 조정
        nums = list(filter(lambda x: x > (int(max(a+b+c)) if c != 'X' else int(max(a+b))), nums))
        if c == 'X': #결과 모르는 식은 따로 저장해둠
            mystery.append(e)
            continue
        #남은 진법으로 수식 계산 -> 맞지 않는 진법 삭제
        tmp_nums = nums.copy()
        for n in nums:
            tmp = eval(str(int(str(a), n)) + op + str(int(str(b), n)))
            if tmp != int(str(c), n):
                tmp_nums.remove(n)
        nums = tmp_nums

    #가능한 진법들과 결과 모르는 식 비교
    #결과값이 유일한지 아닌지 확인, 채워넣기
    for i in range(len(mystery)):
        mys = mystery[i].split(" ")
        a, op, b = mys[0], mys[1], mys[2]
        able_result = []
        for n in nums:
            tmp = eval(str(int(str(a), n)) + op + str(int(str(b), n)))
            tmp = _10toN(tmp, n)
            if tmp not in able_result:
                able_result.append(tmp)

        if len(able_result) == 1: #유일함 - 채워넣기
            if able_result[0] == '':
                able_result[0] = '0'
            mystery[i] = mystery[i].replace('X', str(able_result[0]))
        else: #유일하지 않음 - ?로 채우기
            mystery[i] = mystery[i].replace('X', '?')

    return mystery