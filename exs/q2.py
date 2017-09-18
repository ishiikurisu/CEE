from math import *

def main():
    print('# Q2')

    # Exercise 2

    a = 220.0/110.0
    P = 10
    V = 110.0
    I = 4
    S = P*I
    R = V*V/P
    L = (1/Z/Z - 1/R/R) ** (-0.5)
    print('2. L = %.4f' % (L))

    # Exercise 6

    S = 4E6
    P = 50000
    V = 236000
    I = 4
    a = 230.0 / 138
    Z = V/I
    R = P/I/I
    L = sqrt(Z*Z - R*R)
    L /= 1000 # for kOhm result
    print('6. L = %.4f' % (L))

if __name__ == '__main__':
    main()
