if __name__ == '__main__':
    dice = list(map(int, input().split()))

    if len(set(dice)) == len(dice):
        print(max(dice) * 100)
    else:
        for n in set(dice):
            if dice.count(n) == 3:
                print(10000 + n * 1000)
            elif dice.count(n) == 2:
                print(1000 + n * 100)