def solution(mystr, num1, num2):
    mystr = list(mystr)
    tmp = mystr[num1]
    mystr[num1] = mystr[num2]
    mystr[num2] = tmp
    
    return ''.join(mystr)