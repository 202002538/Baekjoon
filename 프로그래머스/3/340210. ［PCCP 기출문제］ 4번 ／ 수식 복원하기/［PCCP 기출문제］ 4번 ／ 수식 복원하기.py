import sys
input = sys.stdin.readline
import copy

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
        nums = list(filter(lambda x: x > (int(max(a+b+c)) if c != 'X' else int(max(a+b))), nums))
        if c == 'X': 
            mystery.append(e)
            continue
        tmp_nums = nums.copy()
        for n in nums:
            a1, b1, c1 = int(str(a), n), int(str(b), n), int(str(c), n)
            if op == '+':
                tmp = a1 + b1
            else:
                tmp = a1 - b1
            if tmp != c1:
                tmp_nums.remove(n)
        nums = tmp_nums

    for i in range(len(mystery)):
        mys = mystery[i].split(" ")
        a, op, b = mys[0], mys[1], mys[2]
        able_result = []
        for n in nums:
            a1, b1 = int(str(a), n), int(str(b), n)
            if op == '+':
                tmp = a1 + b1
            else:
                tmp = a1 - b1
            tmp = _10toN(tmp, n)
            if tmp not in able_result:
                able_result.append(tmp)
        if len(able_result) == 1:
            if able_result[0] == '':
                able_result[0] = '0'
            mystery[i] = mystery[i].replace('X', str(able_result[0]))
        else:
            mystery[i] = mystery[i].replace('X', '?')

    return mystery