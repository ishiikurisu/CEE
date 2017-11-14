from math import *

def par(a, b):
    return 1/(1/a+1/b)

if __name__ == '__main__':
    w_e = 2*pi*60
    pn = 60
    w_r = 2*pi*114/60
    v = 380

    r_e = 0.2
    x_e = 0.4j
    r_r = 0.2
    x_r = 0.4j
    x_m = 40j
    perdas_rot = 200

    n = w_r
    n_s = w_e/pn
    s = (1800 - 114)/1800
    i_e = v / (r_e + x_e) + (par(x_m, r_r/s + x_r))
    e_2 = v - i_e*(r_e + x_e)
    i_r = e_2 / (r_r/s + x_r)
    pm = r_e * (1-s) * (i_r**2) / s
    p_cr = r_r * (i_r**2)
    p_ef = pm + p_cr
    p_ce = 3*r_e * (i_e**2)
    pq = p_ce + p_ef
    pcv = pm - perdas_rot
    t = pm / w_r
    er = abs(pm)/abs(p_ef)
    cv = 745.7

    print('escorregamento s = %.4f%%' % (s))
    print('corrente no estator i_e = %.4f' % (abs(i_e)))
    print("corrente no rotor i_r = %.4f" % (abs(i_r)))
    print('potencia de entrada pq = %.4f' % (abs(pq)))
    print('perdas no cobre do estator p_ce = %.4f' % (abs(p_ce)*1000))
    print('potencia no entreferro p_ef = %.4f' % (abs(p_ef)*1000))
    print('perdas no cobre do rotor p_cr = %.4f' % (abs(p_cr)*1000))
    print("potencia mecanica convertida pm = %.4f" % (abs(pm)*1000))
    print('potencia mecanica entregue pcv = %.4f' % (abs(pcv)*cv))
    print('conjugado desenvolvido na carga t = %.4f' % (abs(t)))
    print('rendimento er = %.4f' % (100-er*100))
