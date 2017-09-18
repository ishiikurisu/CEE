import cee
import cmath
import math

def q1(s, u, pf, tr, a):
    i = s / u / pf
    return (tr['r_eq']/a) * ((i)**2)

def q2(s, u, pf, tr, a):
    i = s / u / pf
    v = u + ((tr['r_eq']/a) + (1j*tr['x_eq']/a))*i
    im = v / cee.parallel(tr['r_m']/a, 1j*tr['x_m']/a)
    return tr['r_m'] * (im.real**2)

def q3(s, u, pf, tr, a):
    i = s/u/pf
    v = u + ((tr['r_eq']/a) + (1j*tr['x_eq']/a))*i
    z = cee.parallel(tr['r_m']/a, 1j*tr['x_m']/a)
    im = v / z
    pin = (v*(im+i)).real
    pl = tr['p_f'] + tr['p_c']
    return 100 * (1-pl/pin)

def q4(tr):
    return 1-0.92

def q5(tr):
    return (tr['n'] + (100 - tr['reg']))/2

def main():
    print("# Prova 1")

    s_nom = 112500
    u_at = 13800.0
    u_bt = 220.0

    a = u_at / u_bt

    pf = 0.92

    tr_a = { }
    tr_a['r_eq'] = 11.8496
    tr_a['x_eq'] = 13.5424
    tr_a['r_m'] = 372416.0
    tr_a['x_m'] = 135424.0

    tr_b = { }
    tr_b['u_cc'] = 220
    tr_b['i_cc'] = 8.6797
    tr_b['u_ca'] = 220
    tr_b['i_ca'] = 8.1522
    tr_b['p_ca'] = 600
    tr_b['p_cc'] = 900
    tr_b['r_m'] = (tr_b['u_ca']**2) / tr_b['p_ca']
    tr_b['x_m'] = (tr_b['u_ca']**2) / cmath.sqrt(s_nom**2 - (tr_b['u_ca']**2)/tr_b['r_m'])
    tr_b['x_eq'] = (cmath.sqrt((s_nom)**2 - (tr_b['p_cc'])**2) / ((tr_b['i_cc'])**2))
    tr_b['r_eq'] = (tr_b['u_cc'] / (tr_b['i_cc']**2))

    print("Questão 1")
    tr_a['p_f'] = q1(s_nom, u_bt, pf, tr_a, a*a)
    tr_b['p_f'] = q1(s_nom, u_bt, pf, tr_b, 1)
    print("Trafo A: perdas no ferro = %.4f" % (tr_a['p_f']))
    print("Trafo B: perdas no ferro = %.4f" % (tr_b['p_f']))

    print("Questão 2")
    tr_a['p_c'] = q2(s_nom, u_bt, pf, tr_a, a*a)
    tr_b['p_c'] = q2(s_nom, u_bt, pf, tr_b, 1)
    print("Trafo A: perdas no cobre = %.4f" % (tr_a['p_c']))
    print("Trafo B: perdas no cobre = %.4f" % (tr_b['p_c']))

    print("Questão 3")
    tr_a['n'] = q3(s_nom, u_bt, pf, tr_a, a*a)
    tr_b['n'] = q3(s_nom, u_bt, pf, tr_b, 1)
    print("Trafo A: rendimento = %.2f %%" % (tr_a['n']))
    print("Trafo B: rendimento = %.2f %%" % (tr_b['n']))

    print("Questão 4")
    tr_a['reg'] = q4(tr_a)
    tr_b['reg'] = q4(tr_b)
    print("Trafo A: regulação = %.2f %%" % (tr_a['reg']))
    print("Trafo B: regulação = %.2f %%" % (tr_b['reg']))

    print("Questão 5")
    tr_a['pt'] = q5(tr_a)
    tr_b['pt'] = q5(tr_b)
    print("Trafo A: pontuação = %.2f" % (tr_a['pt']))
    print("Trafo B: pontuação = %.2f" % (tr_b['pt']))

if __name__ == '__main__':
    main()
