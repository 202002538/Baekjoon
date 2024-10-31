import sys
input = sys.stdin.readline
import math

def solution(enroll, referral, seller, amount):
    reference = dict(zip(enroll, referral))
    money = dict(zip(enroll, [0] * len(enroll)))

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