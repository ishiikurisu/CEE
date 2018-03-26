from math import pi

__about__ = """
FMM = F*R
FMM = N*I
R = l/A/mu
F = FMM/R
"""

if __name__ == '__main__':
    print('# Questão 1')
    N = 1000
    I = 10
    g1 = 2E-3
    A1 = 0.00015
    m = pi*4E-7
    FMM = N*I
    R = g1/A1/m
    F = FMM/R
    print('fi = {0}mW'.format(F * 1000))
    print()

    print('# Questão 2')
    g1 = 2E-3
    A1 = 0.00035
    R = g1/A1/m
    print('R = {0}MH'.format(R / 1E6))
    print()
