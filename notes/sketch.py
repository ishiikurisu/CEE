from math import pi

if __name__ == '__main__':
    mmHg = 133.32239
    cm = 1.0/100
    s = 1
    D = 3.6 * cm
    F = (33.0 * cm) / (1 * s)
    P_S = 120 * mmHg
    A = pi*((D/2)**2)
    P = 8 * F * P_S * A
    D_L = 265/1.63
    P_V = D_L * (2 * 0.2)
    print("P = F*P_S*A = %.3f" % (P))
    print("P_V = %.3f" % (P_V))
