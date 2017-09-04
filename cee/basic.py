import cmath
import math

def parallel(u, v):
    return 1/(1/u + 1/v)

def from_phasor(r, f):
    return r * (math.cos(math.radians(f)) + 1j * math.sin(math.radians(f)))

def phase(z):
    return math.degrees(cmath.phase(z))
