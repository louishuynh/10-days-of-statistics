if __name__ == '__main__':
    # 1 lines
    # 1st line contains space separated floats

    # method 1 (doesn't seem to work on hacker rank)
    # numbers will look something like [0.88 1.55]
    # lam_1_str, lam_2_str = sys.stdin
    # lam_1, lam_2 = float(lam_1_str), float(lam_2_str)

    lam_1_str, lam_2_str = input().split(' ')
    lam_1, lam_2 = float(lam_1_str), float(lam_2_str)

    print('{:.3f}'.format(160 + 40 * (lam_1 + lam_1 ** 2)))
    print('{:.3f}'.format(128 + 40 * (lam_2 + lam_2 ** 2)))
