if __name__ == '__main__':
    score = input()
    half = len(score) // 2

    left = sum(map(int, score[:half]))
    right = sum(map(int, score[half:]))

    print("LUCKY") if left == right else print("READY")