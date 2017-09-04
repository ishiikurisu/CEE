import cee

print("# 17.8.31")
v1 = cee.from_phasor(2351.08, -35.33)
r = 105800.0
x = 1j*11011
ie = v1 / (cee.parallel(r, x))
print("i_e = %.4f < %.4f" % (abs(ie), cee.phase(ie)))
i2 = cee.from_phasor(6.5217, -36.87)
i1 = i2 + ie
print("i_1 = %.4f < %.4f" % (abs(i1), cee.phase(i1)))
