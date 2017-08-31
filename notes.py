import cmath
import math

def parallel(u, v):
    return 1/(1/u + 1/v)

def from_phasor(r, f):
    return r * (math.cos(math.radians(f)) + 1j * math.sin(math.radians(f)))

if __name__ == '__main__':
    print("# 17.8.31")
    v1 = from_phasor(2351.08, -35.33)
    r = 105800.0
    x = 1j*11011
    ie = v1 / (parallel(r, x))
    print("i_e = %.4f < %.4f" % (abs(ie), math.degrees(cmath.phase(ie))))
    i2 = from_phasor(6.5217, -36.87)
    i1 = i2 + ie
    print("i_1 = %.4f < %.4f" % (abs(i1), math.degrees(cmath.phase(i1))))
