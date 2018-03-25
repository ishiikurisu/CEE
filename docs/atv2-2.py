def par(a, b):
    return 1/(1/a+1/b)

rp = 5
xp = 6
rc = 50E3
rs = 5E-3
xs = 6E-3
xm = 10E3
n = 8000/277

if __name__ == '__main__':
    print("Questão A")
    n2 = n*n
    rp = rp/n2
    xp = xp/n2
    rc = rc/n2
    rs = rs*n2
    xs = xs*n2
    xm = xm/n2
    print('rp = {0} ohm'.format(rp))
    print('xp = {0} ohm'.format(xp))
    print('rc = {0} ohm'.format(rc))
    print('rs = {0} ohm'.format(rs))
    print('xs = {0} ohm'.format(xs))
    print('xm = {0} ohm'.format(xm))
    print()

    print("Questão B")
    v2 = 277
    v1 = n*v2
    print('v1 = {0}V'.format(v1))
    print()

    print("Questão C")
    e = v1*n2/(rp+1j*xp)
    d = 1 + par(1j*xm, rc)/(rp+1j*xp) + par(1j*xm, rc)/n2/(rs+1j*xs)
    ic = e/d
    perdas = par(1j*xm, rc)*ic*ic/n2
    print('perdas no cobre = {0}W'.format(perdas.real))
    print('perdas no núcleo = {0}W'.format(perdas.imag))
    print()
