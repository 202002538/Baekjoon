import sys
input = sys.stdin.readline

def solution(bin1, bin2):
    answer = ''
    maxlen = max(len(bin1), len(bin2))
    bin1 = bin1.zfill(maxlen)
    bin2 = bin2.zfill(maxlen)
    adder = [0] * (maxlen+1)

    for i in range(1, maxlen+1):
        idx = -1 * i
        if bin1[idx] == '1' and bin2[idx] == '1':
            if adder[idx] == 1:
                answer = '1' + answer
                adder[idx - 1] = 1
            else:
                answer = '0' + answer
                adder[idx - 1] = 1
        elif bin1[idx] == '0' and bin2[idx] == '0':
            if adder[idx] == 1:
                answer = '1' + answer
            else:
                answer = '0' + answer
        else:
            if adder[idx] == 1:
                answer = '0' + answer
                adder[idx-1] = 1
            else:
                answer = '1' + answer

    if adder[idx-1] == 1:
        answer = '1' + answer
    return answer