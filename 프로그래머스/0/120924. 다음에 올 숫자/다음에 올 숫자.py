def solution(comm):
    if comm[1] - comm[0] == comm[2] - comm[1]:
        return comm[-1] + (comm[1] - comm[0])
    else:
        return comm[-1] * (comm[1] / comm[0])
