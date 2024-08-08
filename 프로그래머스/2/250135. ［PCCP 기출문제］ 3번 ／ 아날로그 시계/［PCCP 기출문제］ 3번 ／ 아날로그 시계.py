import sys
input = sys.stdin.readline

def solution(h1, m1, s1, h2, m2, s2):
    def CountFromMidnight(h, m, s):
        h_degree = (h*30+m*0.5+s*0.5/60)%360
        m_degree = (m*6+s*0.1)%360
        s_degree = s*6
        result = -1

        if s_degree >= m_degree:
            result += 1
        if s_degree >= h_degree:
            result += 1

        result += (h*60+m)*2
        result -= h
        if h >= 12:
            result -= 2
        return result

    ret = CountFromMidnight(h2, m2, s2) - CountFromMidnight(h1, m1, s1)
    if (h1 == 0 or h1 == 12) and m1 == 0 and s1 == 0:
        ret += 1
    return ret
