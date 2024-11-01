def solution(A, B):
    A, B = list(A), list(B)
    
    for i in range(len(A)):
        if A == B:
            return i
        A = [A[-1]] + A[:-1]
        
    return -1 