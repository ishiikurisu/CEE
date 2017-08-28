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
        c = 1 / (2 * cmath.pi * 60 * inlet['l'])

    z = r + 1j * l
    if c > 0:
        z += 1j / c

    i = v / z
    s = v * star(i)
    w = abs(s)
    p = s.real
    q = s.imag
    pf = p / cmath.sqrt(p**2 + q**2)

    outlet['z'] = z
    outlet['i'] = i
    outlet['s'] = s
    outlet['w'] = w
    outlet['q'] = q
    outlet['pf'] = pf
    return outlet

def display(what, data):
    print('--- # '+ what)
    for key in data:
        it = complex(data[key])
        line = '%s = %.2f + j%.2f' % (key, it.real, it.imag)
        print(line)
    print('...')

if __name__ == '__main__':
    display('Ensaio 3', theory({
        'v': 200,
        'r': 485,
        'l': 0.585
    }))
