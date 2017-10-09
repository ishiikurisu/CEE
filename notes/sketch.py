if __name__ == '__main__':
    mmHg = 133.32239
    cm = 1.0/100
    s = 1
    F = (33.0 * cm) / (1 * s)
    P_S = 120 * mmHg
    P = 8 * F * P_S
    print("P = F*P_S = %.3f" % (P))
