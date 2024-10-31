import sys
input = sys.stdin.readline
import math

def solution(enroll, referral, seller, amount):
    level = dict(zip(enroll, [1] * len(enroll)))
    reference = dict(zip(enroll, referral))
    money = dict(zip(enroll, [0] * len(enroll)))

    for i, r in enumerate(referral):
        if r != '-':
            level[enroll[i]] = level[r] + 1

    def get_money(name, earn):
        tax = int(earn / 10)
        money[name] += earn - tax
        if tax != 0 and reference[name] != '-':
            get_money(reference[name], tax)


    for sell, am in zip(seller, amount): 
        get_money(sell, am*100)

    answer = []
    for e in enroll:
        answer.append(money[e])

    return answer