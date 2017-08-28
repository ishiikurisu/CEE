import cmath

def star(z):
    return z.real - 1j*z.imag

def theory(inlet):
    outlet = { }
    v = inlet['v']
    r = inlet['r']
    l = 0
    c = 0

    if 'l' in inlet:
        l = 2 * cmath.pi * 60 * inlet['l']
    if 'c' in inlet:
        c = 1 / (2 * cmath.pi * 60 * inlet['c'])

    z = r + 1j * l
    if c > 0:
        z += -1j * c

    i = v / z
    s = v * star(i)
    w = abs(s)
    p = s.real
    q = s.imag
    pf = p / cmath.sqrt(p**2 + q**2)

    outlet['v'] = v
    outlet['r'] = r
    outlet['l'] = l
    outlet['c'] = c
    outlet['z'] = z
    outlet['i'] = i
    outlet['s'] = s
    outlet['w'] = w
    outlet['q'] = q
    outlet['pf'] = pf
    return outlet

def practice(inlet):
    outlet = { }
    v = inlet['v']
    w = inlet['w']
    i = inlet['i']

    # TODO Understand what W, S, P and Q are. This still is really fuzzy.

    outlet['v'] = v
    outlet['w'] = w
    outlet['i'] = i

    return outlet

def display(what, data):
    print('--- # '+ what)
    for key in data:
        it = complex(data[key])
        line = '%s = %.6f + j%.6f' % (key, it.real, it.imag)
        print(line)
    print('...')

if __name__ == '__main__':
    display('Ensaio 3', theory({
        'v': 200,
        'r': 485,
        'l': 0.585
    }))
    display('Pratica 3', practice({
        'v': 200.1,
        'w': 85,
        'i': 0.754
    }))
    display('Ensaio 4', theory({
        'v': 200,
        'r': 485,
        'l': 0.585,
        'c': 12e-6
    }))
