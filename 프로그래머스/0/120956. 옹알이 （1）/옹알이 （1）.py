def solution(babbling):
    answer = 0
    while babbling:
        b = babbling.pop()
        if b in ["aya", "ye", "woo", "ma"]:
            answer += 1
        elif b.startswith(("aya", "woo")):
            babbling.append(b[3:])
        elif b.startswith(("ye", "ma")):
            babbling.append(b[2:])
    return answer