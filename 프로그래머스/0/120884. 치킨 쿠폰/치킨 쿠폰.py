def solution(chicken):
    answer = 0
    coupon = chicken
    
    while coupon // 10 != 0:
        order = coupon // 10
        answer += order
        coupon = coupon % 10
        coupon += order
    
    
    return answer