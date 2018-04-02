__about__ = """
B = 1T inside
R = 0.3ohm
l = 1m
T = 110V
F = ?N
i(0) = ?A
v(inf) = ?m/s
W <- 40N => v(inf) = ?m/s
eff = ?%
"""

__calcs__ = """
F = Bil
e = vBl
T = Ri + e <=> i = (T - e)/R
e(0) = 0
e(inf) = T
v = Bl/e
P = F*v =>
T*v = (T-W)*u => u = (T*v)/(T-W)
"""

B = 1
R = 0.3
l = 1
T = 110
W = 40

if __name__ == '__main__':
    print("---")
    i = T/R
    F = B*i*l
    print('F = {0}N'.format(F))
    print('i = {0}A'.format(i))
    v = B*l/T
    print('v(inf) = {0}m/s'.format(v))
    print('--- # W <- 40N')
    v = (T*v)/(T+W)
    print('v(inf) <- {0}m/s'.format(v))
    print('...')
