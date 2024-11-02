import math
def solution(num, total):
    start = math.ceil(total / num) - math.floor(num / 2)
    
    return [i for i in range(start, (start+num))]